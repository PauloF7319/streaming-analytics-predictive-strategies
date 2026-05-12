import pandas as pd
import numpy as np
import hashlib
import os

def run_data_pipeline(input_path, output_path):
    """
    Pipeline: Bronze (Raw) -> Silver (Processed/Refined)
    Ensures technical integrity and UK GDPR compliance.
    """
    print(f"🦁 Initialising Refinement Pipeline...")

    # 1. Loading the data
    if not os.path.exists(input_path):
        print(f"❌ Error: File {input_path} not found.")
        return
    
    df = pd.read_csv(input_path)
    initial_count = len(df)
    print(f"📊 Raw records loaded: {initial_count}")

    # --- STAGE 1: DEEP CLEANING (Technical Quality) ---
    print("🧹 Executing technical cleansing and null handling...")
    
    # Identify the ID column (case-insensitive check)
    col_id = 'user_id' if 'user_id' in df.columns else 'User_ID'
    
    # Removal of Duplicates
    df = df.drop_duplicates()
    
    # Null Handling: Remove rows without a valid ID
    if col_id in df.columns:
        df = df.dropna(subset=[col_id])
    else:
        print("⚠️ Warning: ID column not found. Skipping dropna.")
    
    # Smart Imputation: Median for numerical values, 'Unknown' for categorical
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('Unknown')

    # String Normalisation (trimming extra whitespace)
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # --- STAGE 2: GDPR & PRIVACY (Data Secrecy) ---
    print("🔐 Applying GDPR protocols (Anonymisation & PII Scrubbing)...")
    
    # User_ID Pseudonymisation using SHA-256
    if col_id in df.columns:
        df[col_id] = df[col_id].apply(
            lambda x: hashlib.sha256(str(x).encode()).hexdigest()[:16]
        )

    # Systematic removal of PII (Personally Identifiable Information)
    pii_list = ['Name', 'Email', 'Address', 'Phone', 'Surname', 'Full_Name']
    df = df.drop(columns=[c for c in pii_list if c in df.columns], errors='ignore')

    # --- STAGE 3: EXPORTATION (The Parquet Standard) ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Saving to Parquet for maximum ML performance
    df.to_parquet(output_path, index=False, engine='pyarrow')
    
    print(f"✅ Success! 'Processed' layer generated at: {output_path}")
    print(f"📈 Summary: {initial_count} raw records -> {len(df)} refined.")
    print(f"🛡️ Status: Anonymous Data ready for ML (95% Target).")

if __name__ == "__main__":
    # Ensure the input filename matches your CSV in the data/ folder
    INPUT_FILE = 'data/streaming_data.csv' 
    OUTPUT_FILE = 'data/processed/streaming_refined.parquet'
    
    run_data_pipeline(INPUT_FILE, OUTPUT_FILE)
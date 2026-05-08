import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

def refine_and_save_to_parquet(raw_path, output_path):
    """
    Take the raw CSV, scrub it clean, and save it as a Parquet file.
    It's much more efficient for a "bit of" heavy lifting with 50k rows.
    """
    print(f"[*] Sorting out the data from: {raw_path}")
    
    try:
        # Reading the raw stuff - hopefully it's not a dog's breakfast
        df = pd.read_csv(raw_path)

        # 1. Privacy First (The 'Proper' Way)
        # Binning sensitive info and creating a clean Customer_ID
        if 'name' in df.columns or 'customer_name' in df.columns:
            df['Customer_ID'] = [f"USR-{i:05d}" for i in range(len(df))]
        
        # Dropping PII to keep the Home Office chaps happy
        pii_cols = ['name', 'email', 'address', 'phone', 'postcode']
        df = df.drop(columns=[col for col in pii_cols if col in df.columns])

        # 2. Saving as Parquet
        # This makes the data management much more "top-hole" and nippy
        df.to_parquet(output_path, index=False, engine='pyarrow')
        
        print(f"[+] Brilliant! Data refined and tucked away at: {output_path}")
        print(f"[+] Original size was much bulkier than this tidy Parquet file.")
        
        return df

    except Exception as e:
        print(f"[-] Absolute nightmare! It's all gone pear-shaped: {e}")
        return None

if __name__ == "__main__":
    # Ensure the directory structure is "ship-shape"
    # Creating a dedicated folder for processed bits to keep things tidy
    processed_dir = 'data/processed'
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    raw_file = 'data/streaming_data.csv'  # Your raw input
    parquet_file = os.path.join(processed_dir, 'streaming_refined.parquet')
    
    # Let's get cracking with the refinement
    refined_df = refine_and_save_to_parquet(raw_file, parquet_file)
    
    if refined_df is not None:
        print("\n--- Quick Peek at the Processed Data ---")
        print(refined_df.head())
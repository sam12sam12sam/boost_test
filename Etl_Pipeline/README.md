## How to Run

1. Start MySQL 
2. Create schema using sql/schema.sql
3. Open Google Colab
4. setup the connection between mysql and google colab using ngrok
5. Run notebooks/run_etl.ipynb

## Expected Output
- Tables populated:
  - test
  - users
  - telephone_numbers
  - jobs_history
- PII masked
- Foreign keys enforced

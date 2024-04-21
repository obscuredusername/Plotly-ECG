import psycopg2

# Function to connect to PostgreSQL database and fetch data
def fetch_selected_data():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="ECG",
            user="postgres",
            password="1234",
            host="127.0.0.1",
            port="5432"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute a query to fetch file number, gender, and diseases
        cur.execute('SELECT * FROM public."ECG"')

        # Fetch all rows from the result set
        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]

        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return the fetched data and headers
        return rows, headers

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
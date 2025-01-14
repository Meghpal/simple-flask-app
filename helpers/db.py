import sqlite3


connection = sqlite3.connect("database/reviews.db")

initializer = connection.cursor()
initializer.execute(
    """
    CREATE TABLE IF NOT EXISTS
    REVIEWS_DATA (
        REV_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        REVIEW VARCHAR(500) NOT NULL,
        PREDICTION VARCHAR(20) NOT NULL,
        FEEDBACK VARCHAR(10) CHECK (FEEDBACK in ('correct','wrong')) NULL
    );
    """
)

connection.commit()
initializer.close()
connection.close()


def execute(sql_command, fetchAll=False):
    connection = sqlite3.connect("database/reviews.db")
    cursor = connection.cursor()
    result = ""

    try:
        cursor.execute(sql_command)
    except Exception as e:
        result = "Error: " + str(e)
    else:
        connection.commit()

        if fetchAll:
            result = cursor.fetchall()
        else:
            result = cursor.lastrowid
    finally:
        cursor.close()
        connection.close()
        return result


def get_pending_feedback():
    result = execute(
        """
        SELECT * FROM REVIEWS_DATA
        WHERE FEEDBACK IS NULL
        """,
        True,
    )

    response = []
    for row in result:
        response.append(row)

    return response


def get_data():
    result = execute(
        """
        SELECT * FROM REVIEWS_DATA
        """,
        True,
    )

    response = []
    for row in result:
        response.append(row)

    return response


def add_row(review, prediction):
    return execute(
        f"""
        INSERT INTO REVIEWS_DATA
            (REVIEW, PREDICTION)
        VALUES
            ("{review}", "{prediction}")
        """
    )


def update_feedback(rid, feedback):
    return execute(
        f"""
        UPDATE REVIEWS_DATA
        SET
            FEEDBACK = "{feedback}"
        WHERE
            REV_ID = {rid}
        """
    )
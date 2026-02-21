import mysql.connector

# connect to mysql
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bhavasql@0906",   # change this
    database="dev_bugtracker_system"
)

cursor = conn.cursor()

print("connected to dev_bugtracker_system successfully!\n")


# -----------------------------
# create bug
# -----------------------------
def create_bug():
    title = input("enter bug title: ")
    description = input("enter description: ")
    priority = input("enter priority (low/medium/high): ")
    project_id = int(input("enter project id: "))
    assigned_to = int(input("enter user id: "))

    query = """
    insert into bugs (title, description, priority, project_id, assigned_to)
    values (%s, %s, %s, %s, %s)
    """

    values = (title, description, priority, project_id, assigned_to)

    cursor.execute(query, values)
    conn.commit()

    print("bug added successfully!\n")


# -----------------------------
# view bugs (with join)
# -----------------------------
def view_bugs():
    query = """
    select 
    b.bug_id,
    b.title,
    b.status,
    b.priority,
    u.name,
    p.project_name
    from bugs b
    join users u on b.assigned_to = u.user_id
    join projects p on b.project_id = p.project_id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n---- bug list ----")
    for row in results:
        print(row)
    print()


# -----------------------------
# update bug status
# -----------------------------
def update_bug_status():
    bug_id = int(input("enter bug id: "))
    status = input("enter new status (open/in progess/resolved): ")

    query = "update bugs set status=%s where bug_id=%s"
    cursor.execute(query, (status, bug_id))
    conn.commit()

    print("bug status updated!\n")


# -----------------------------
# delete bug
# -----------------------------
def delete_bug():
    bug_id = int(input("enter bug id to delete: "))

    query = "delete from bugs where bug_id=%s"
    cursor.execute(query, (bug_id,))
    conn.commit()

    print("bug deleted successfully!\n")


# -----------------------------
# main menu
# -----------------------------
while True:
    print("1. create bug")
    print("2. view bugs")
    print("3. update bug status")
    print("4. delete bug")
    print("5. exit")

    choice = input("enter choice: ")

    if choice == "1":
        create_bug()
    elif choice == "2":
        view_bugs()
    elif choice == "3":
        update_bug_status()
    elif choice == "4":
        delete_bug()
    elif choice == "5":
        break
    else:
        print("invalid choice\n")

conn.close()
print("connection closed.")
import streamlit as st
import pandas as pd

if 'employee_data' not in st.session_state:
    st.session_state.employee_data = pd.DataFrame(columns=["Empno", "Ename", "Job", "Deptno"])
if 'department_data' not in st.session_state:
    st.session_state.department_data = pd.DataFrame(columns=["Deptno", "Dname", "Loc"])

def page_employee_data_entry():
    st.title("Employee Data Entry")
    empno = st.text_input("Employee Number (Empno)")
    ename = st.text_input("Employee Name (Ename)")
    job = st.text_input("Job")
    deptno = st.text_input("Department Number (Deptno)")
    
    if st.button("Submit"):
        if empno and ename and job and deptno:
            st.session_state.employee_data.loc[len(st.session_state.employee_data)] = [empno, ename, job, deptno]
            st.success("Employee data submitted successfully!")
        else:
            st.error("Please fill in all the fields.")

def page_department_data_entry():
    st.title("Department Data Entry")
    deptno = st.text_input("Department Number (Deptno)")
    dname = st.text_input("Department Name (Dname)")
    loc = st.text_input("Location (Loc)")
    
    if st.button("Submit"):
        if deptno and dname and loc:
            st.session_state.department_data.loc[len(st.session_state.department_data)] = [deptno, dname, loc]
            st.success("Department data submitted successfully!")
        else:
            st.error("Please fill in all the fields.")

def page_visualization():
    st.title("Joined Employee and Department Data")
    
    joined_data = st.session_state.employee_data.merge(st.session_state.department_data, on="Deptno", how="left")
    
    st.dataframe(joined_data)

def main():
    st.sidebar.title("Data Entry App")
    page = st.sidebar.radio("Select a page:", [ "Department Data Entry", "Employee Data Entry", "Visualization"])
    
    if page == "Employee Data Entry":
        page_employee_data_entry()
    elif page == "Department Data Entry":
        page_department_data_entry()
    elif page == "Visualization":
        page_visualization()

if __name__ == "__main__":
    main()



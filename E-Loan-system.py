from flask import Flask, render_template, redirect, request, session, url_for, json, Response
import psycopg2

app = Flask(__name__)
app.secret_key = 'development'

# database connection
try:
    conn_string = "host = 'localhost' dbname = 'e_loan_system' user = 'postgres' password = 'root'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print "DataBase Successfully Connected"

    # load the default page
    @app.route('/')
    def index():
        return render_template('login.html')

    # check the session
    @app.route('/login_user')
    def login_users():
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        else:
            return render_template('index.html')

    # login to the system
    @app.route('/login_user', methods=['POST'])
    def login_user():
        user_name = request.form['user_name']
        password = request.form['password']
        error = None
        sql = "select user_name, password,department from user_register where user_name='" + user_name + "'and password='" + password + "'"
        cursor.execute(sql)
        conn.commit()
        value = cursor.fetchall()
        if not value:
            error = 'Invalid Username or Password'
            return render_template('login.html', error=error)
        elif value:
            user_category = value[0][2].strip()
            if request.method == 'POST':
                session['logged_in'] = True
                session['user_role'] = value[0][2].strip()
                if user_category == 'admin':
                    return render_template('index.html')
                elif user_category == 'manager':
                    return render_template('index2.html')
                elif user_category == 'front_desk':
                    return render_template('index3.html')
            return render_template('index.html')


    # user register
    @app.route('/user_register', methods=['POST'])
    def user_register():
        try:
            user_name = request.form['user_name']
            password = request.form['password']
            Dpartmnt = request.form['department']
            Nic_Number = request.form['nic']
            sql = """INSERT INTO user_register(user_name, password, department, nic) VALUES ('%s', '%s', '%s', '%s')""" % (
                user_name,
                password,
                Dpartmnt,
                Nic_Number)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('user_reg'))
        except:
            print"Error"
            return redirect(url_for('error'))

 # tc for client
    @app.route('/tc_register', methods=['POST'])
    def tc_register():
        try:
            client_id = request.form['client_nic']
            amount = request.form['amount']
            period = request.form['period']
            rate = request.form['rate']
            InsVal = request.form['InsVal']
            totalint = request.form['totalint']
            totalamount = request.form['totalamount']
            sql = """INSERT INTO tc_for_client(client_nic, loan_amount, loan_period, rate, installment, interest, total_amount) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                client_id,
                amount,
                period,
                rate,
                InsVal,
                totalint,
                totalamount)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('client_tc'))
        except:
            print"Error"
            return redirect(url_for('error'))



                # client register
    @app.route('/client_register', methods=['POST'])
    def client_register():
        try:
            first_name = request.form['f_name']
            mid_name = request.form['m_name']
            last_name = request.form['l_name']
            nic_number = request.form['nic']
            date_of_birth = request.form['dob']
            email = request.form['email']
            phone_no = request.form['pnom']
            address1 = request.form['address1']
            address2 = request.form['address2']
            province = request.form['province']
            district = request.form['district']
            office_add = request.form['of_address']
            contact_no = request.form['cnom']
            gender = request.form['gender']
            maritical = request.form['maritical']
            sql = """INSERT INTO client_register(f_name, mid_name, last_name, nic,   dob, email, phone_no, address1, address2, province, district, office_add, con_no, gender, maritical) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                first_name,
                mid_name,
                last_name,
                nic_number,
                date_of_birth,
                email,
                phone_no,
                address1,
                address2,
                province,
                district,
                office_add,
                contact_no,
                gender,
                maritical)

            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('client_reg'))
        except:
            print"Error"
            return redirect(url_for('error'))

    # client register for loan
    @app.route('/register_loan', methods=['POST'])
    def register_loan():
        try:
            client_name = request.form['client_name']
            client_nic = request.form['client_nic']
            trial_id = request.form['trial_id']
            loan_type = request.form['loan_type']
            amount = request.form['amount']
            period = request.form['period']
            rate = request.form['rate']
            InsVal = request.form['InsVal']
            totalint = request.form['totalint']
            totalamount = request.form['totalamount']
            status = request.form['status']
            sql = """INSERT INTO loan_register(client_name, client_nic, trial_id, loan_type, loan_amount,   loan_period, rate, installment, interest, total_amount,status  ) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                client_name,
                client_nic,
                trial_id,
                loan_type,
                amount,
                period,
                rate,
                InsVal,
                totalint,
                totalamount,
                status)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('loan_reg'))
        except:
            print"Error"
            return redirect(url_for('error'))

# apprual
    @app.route('/apprual', methods=['POST'])
    def apprual():
        try:
            c_name = request.form['c_name']
            c_nic = request.form['c_nic']
            tc_id = request.form['tc_id']
            l_type = request.form['l_type']
            l_amo = request.form['l_amo']
            l_per = request.form['l_per']
            rate = request.form['rate']
            installment = request.form['installment']
            interest = request.form['interest']
            to_amo = request.form['to_amo']
            status = request.form['status']
            sql = """INSERT INTO apprual_form(client_name, client_nic, trial_id, loan_type, loan_amount,   loan_period, rate, installment, interest, total_amount, statuss   ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                c_name,
                c_nic,
                tc_id,
                l_type,
                l_amo,
                l_per,
                rate,
                installment,
                interest,
                to_amo,
                status)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('approved_loan'))
        except:
            print"Error"
            return redirect(url_for('error'))

 # register new loan type
    @app.route('/loan_type', methods=['POST'])
    def loan_type():
        try:
            loan_id = request.form['l_id']
            loan_type = request.form['l_type']
            period = request.form['period']
            max_rate = request.form['mx_rate']
            min_rate = request.form['mn_rate']
            sql = """INSERT INTO loan_type( loan_type, loan_id, period, max_rate, min_rate) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (
                loan_id,
                loan_type,
                period,
                max_rate,
                min_rate)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('new_lo'))
        except:
            print"Error"
            return redirect(url_for('error'))


    # Show data users
    @app.route('/view_user', methods=['GET', 'POST'])
    def view_user():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM user_register"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('view_user.html', values=values)

    # Show data client
    @app.route('/view_cient', methods=['GET', 'POST'])
    def view_cient():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM client_register"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('view_client.html', values=values)

    # Show data users
    @app.route('/view_tc_client', methods=['GET', 'POST'])
    def view_tc_client():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM tc_for_client"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('view_user.html', values=values)

# approved
    @app.route('/approved_loan', methods=['GET', 'POST'])
    def approved_loan():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM apprual_form"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('approved_loan.html', values=values)

# appruval
    @app.route('/view_apprual', methods=['GET', 'POST'])
    def view_apprual():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM loan_register"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('appruval.html', values=values)


    #shoew front desk user
    @app.route('/view_fr_user', methods=['GET', 'POST'])
    def view_fr_user():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM user_register"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('fr_view_user.html', values=values)

#show front desk client
    @app.route('/view_fr_client', methods=['GET', 'POST'])
    def view_fr_client():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM client_register"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('fr_view_client.html', values=values)

# show new loan type
    @app.route('/show_loan', methods=['GET', 'POST'])
    def show_loan():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM loan_type"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('view_loan_type.html', values=values)


    # user action
    @app.route('/user_button_act', methods=['POST', 'GET'])
    def button_act():
        if request.method == 'POST' and request.form['submit'] == 'Modify':
            return modify_user()
        elif request.method == 'POST' and request.form['submit'] == 'Delete':
            return delete_user()

    # client action
    @app.route('/client_bt', methods=['POST', 'GET'])
    def client_bt():
        if request.method == 'POST' and request.form['submit'] == 'Modify':
            return modify_client()
        elif request.method == 'POST' and request.form['submit'] == 'Delete':
            return delete_client()


    # Modify user Data
    @app.route('/modify_user', methods=['POST'])
    def modify_user():
        # get values from the form
        id = request.form['id']
        user_name = request.form['user_name']
        password = request.form['password']
        department = request.form['department']
        nic = request.form['nic']

        try:
            # update query
            update_query = "UPDATE user_register SET user_name = '" + user_name + "', password = '" + password + "', department = '" + department + "', nic = '" + nic + "'  WHERE id = '" + id + "'"
            cursor.execute(update_query)
            conn.commit()
            print "Update Successful"
            return redirect(url_for('view_user'))
        except:
            print "Error"
            return redirect(url_for('home'))

 # Modify client Data
    @app.route('/modify_client', methods=['POST'])
    def modify_client():
        # get values from the form
        id = request.form['id']
        f_name = request.form['f_name']
        m_name = request.form['m_name']
        l_name = request.form['l_name']
        nic = request.form['nic']
        dob = request.form['dob']
        email = request.form['email']
        pnom = request.form['pnom']
        address1 = request.form['address1']
        address2 = request.form['address2']
        province = request.form['province']
        district = request.form['district']
        of_address = request.form['of_address']
        cnom = request.form['cnom']
        gender = request.form['gender']
        maritical = request.form['maritical']

        try:
            # update query
            update_query = "UPDATE client_register SET f_name = '" + f_name + "', mid_name = '" + m_name + "', last_name = '" + l_name + "', nic = '" + nic + "', dob = '" + dob + "', email = '" + email + "', phone_no = '" + pnom + "', address1 = '" + address1 + "', address2 = '" + address2 + "', province = '" + province + "', district = '" + district + "', office_add = '" + of_address + "', con_no = '" + cnom + "', gender = '" + gender + "', maritical = '" + maritical + "'  WHERE id = '" + id + "'"
            cursor.execute(update_query)
            conn.commit()
            print "Update Successful"
            return redirect(url_for('view_cient'))
        except:
            print "Error"
            return redirect(url_for('home'))


    # Delete user
    @app.route('/delete_user', methods=['POST'])
    def delete_user():
        id = request.form['id']
        try:
            delete_query = "DELETE FROM user_register WHERE id = '" + id + "'"
            cursor.execute(delete_query)
            conn.commit()
            print "Successfully Deleted"
            return redirect(url_for('view_user'))
        except:
            print "Error"
            return redirect(url_for('home'))



                # Delete client
    @app.route('/delete_client', methods=['POST'])
    def delete_client():
        id = request.form['id']
        try:
            delete_query = "DELETE FROM client_register WHERE id = '" + id + "'"
            cursor.execute(delete_query)
            conn.commit()
            print "Successfully Deleted"
            return redirect(url_for('view_cient'))
        except:
            print "Error"
            return redirect(url_for('home'))


    # load data into drop down list
    @app.route('/drop_down')
    def drop_down():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT fname FROM users"
        cursor.execute(select_query)
        value = cursor.fetchall()
        return render_template('drop_down.html', values=value)

    # user register
    @app.route('/user_reg')
    def user_reg():
        return render_template('user_registation.html')


    # client register
    @app.route('/client_reg')
    def client_reg():
        return render_template('client_registation.html')

# new loan type
    @app.route('/new_lo')
    def new_lo():
        return render_template('new_loan_types.html')


    # trial cal for client
    @app.route('/client_tc')
    def client_tc():
        return render_template('trial_cal_for client.html')


    # home
    @app.route('/home')
    def home():
        return render_template('index.html')

#index 2
    @app.route('/home_m')
    def home_m():
        return render_template('index2.html')

#index 3
    @app.route('/home_f')
    def home_f():
        return render_template('index3.html')

# appruval
    @app.route('/approve_loan')
    def approve_loan():
        return render_template('appruval.html')


    # view user
    @app.route('/user_view')
    def user_view():
        return render_template('view_user.html')
        # view user

# error page
    @app.route('/error')
    def error():
        return render_template('error_page.html')

# front_desk page
    @app.route('/fr_client_view')
    def fr_client_view():
        return render_template('fr_view_client.html')

# front_desk page
    @app.route('/fr_user_view')
    def fr_user_view():
        return render_template('fr_view_user.html')

# register for loan
    @app.route('/loan_reg')
    def loan_reg():
        return render_template('reg_for_loan.html')

# pi chart
    @app.route('/pypline')
    def pypline():
        try:
            if not session.get('logged_in'):
                return render_template('login.html')
            sql = "select statuss vc, count(*) from apprual_form group by statuss"
            cursor.execute(sql)
            data = cursor.fetchall()
            # return data
            return render_template('pipeline.html', data=data)

        except Exception as e:
            return (str(e))


            # trial cal
    @app.route('/trial_cal')
    def trial_cal():
        return render_template('trial_cal.html')

    # Show data loan register
    @app.route('/view_loan_reg', methods=['GET', 'POST'])
    def view_loan_reg():
        if not session.get('logged_in'):
            return render_template('index.html')
        sql = "SELECT * FROM client_register"
        cursor.execute(sql)
        conn.commit()
        values = cursor.fetchall()
        return render_template('reg_for_loan.html', values=values)


    # logout from the system
    @app.route('/logout')
    def logout():
        session['logged_in'] = False
        session.pop = ['logged_in', None]
        session.clear()
        return redirect(url_for('index'))

    # clear the cache after logout
    @app.after_request
    def add_header(response):
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        return response

    if __name__ == '__main__':
        app.run(debug=True)

except:
    print "Connection Failed"





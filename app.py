from flask import Flask, render_template, request

app = Flask(__name__)

# Data for projects, structured by technology
projects = {
    'Java': [
        {
            'name': 'Online Banking System',
            'objective': 'To create a user-friendly online banking interface that allows users to manage their finances including account management, transactions, and viewing statements.',
            'technologies': 'Java, JDBC, MySQL',
            'features': 'Account creation, money transfer, balance checks, transaction history.',
            'outcome': 'Enhanced user experience with secure and efficient banking operations.'
        },
        {
            'name': 'Inventory Management System',
            'objective': 'To develop a system for managing inventory levels, orders, sales, and deliveries.',
            'technologies': 'Java, JavaFX, SQLite',
            'features': 'Product addition, inventory tracking, order processing, and sales reporting.',
            'outcome': 'Improved accuracy and real-time inventory tracking, leading to better decision making in stock management.'
        }
    ],
    'Node.js': [
        {
            'name': 'E-commerce Website',
            'objective': 'To build a full-featured e-commerce platform for online shopping.',
            'technologies': 'Node.js, Express, MongoDB',
            'features': 'Product listings, shopping cart, checkout process, user authentication.',
            'outcome': 'Delivered a scalable website that supports high user traffic with secure transaction capabilities.'
        },
        {
            'name': 'Chat Application',
            'objective': 'To create a real-time chat application for community interaction.',
            'technologies': 'Node.js, Socket.IO, React',
            'features': 'Instant messaging, group chats, user status updates.',
            'outcome': 'Provided a platform for instant communication with low latency, enhancing user engagement.'
        }
    ],
    'C++': [
        {
            'name': 'Traffic Simulation System',
            'objective': 'To simulate traffic flow and optimize traffic light timings.',
            'technologies': 'C++, OpenGL',
            'features': 'Real-time traffic simulation, adjustable parameters for traffic density and timings.',
            'outcome': 'Optimized traffic flow in simulations, potentially reducing real-world traffic congestion.'
        },
        {
            'name': 'Bank Management System',
            'objective': 'To develop a console-based application for managing a bank’s operations.',
            'technologies': 'C++',
            'features': 'Account management, transaction processing, and customer details management.',
            'outcome': 'Streamlined bank operations and improved efficiency in handling customer transactions.'
        }
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects_view():
    return render_template('projects.html')

@app.route('/education')
def education_view():
    return render_template('education.html')

@app.route('/certifications')
def certifications_view():
    return render_template('certifications.html')

if __name__ == '__main__':
    app.run(debug=True)
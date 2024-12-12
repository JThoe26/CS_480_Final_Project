from flask import Flask, request, jsonify

app = Flask(__name__)

notifications = []

# Reads all notifications
@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)

# crates a new notification
@app.route('/notifications/create', methods=['POST'])
def create_notification():
    data = request.get_json()
    notification = {
        'id': len(notifications) + 1,
        'message': data['message']
    }
    notifications.append(notification)
    return jsonify(notification), 201

# Deletes a specified notification
@app.route('/notifications/delete/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    global notifications
    notifications = [n for n in notifications if n['id'] != notification_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
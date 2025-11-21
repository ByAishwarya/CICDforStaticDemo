import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log when Lambda starts
    print("🚀 Lambda function started execution")
    logger.info("🔵 Lambda handler called")
    
    # Log the incoming event
    print("📦 Received event:", json.dumps(event))
    logger.info("📦 Event details: %s", event)
    
    # Log request method and path (if available)
    if 'httpMethod' in event:
        print(f"🌐 HTTP Method: {event['httpMethod']}")
        logger.info(f"🌐 HTTP Method: {event['httpMethod']}")
    
    if 'path' in event:
        print(f"📍 Path: {event['path']}")
        logger.info(f"📍 Path: {event['path']}")
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Website</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: magenta; }
            .container { max-width: 800px; margin: 0 auto; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from AWS Lambda!</h1>
            <p>This HTML is served directly from my Lambda function.</p>
            <p>Created by Aishwarya</p>
            
            <h2>User Form</h2>
            <form>
                <p><strong>Name:</strong> <input type="text" id="name" required></p>
                <p><strong>Email:</strong> <input type="email" id="email" required></p>
                <button type="button" onclick="submitForm()">Submit</button>
            </form>
            
            <div id="result" style="margin-top: 20px;"></div>
            
            <script>
                function submitForm() {
                    const name = document.getElementById('name').value;
                    const email = document.getElementById('email').value;
                    
                    const data = {
                        name: name,
                        email: email
                    };
                    
                    // Send to another Lambda or process data
                    alert('Name: ' + name + ', Email: ' + email);
                    document.getElementById('result').innerHTML = 
                        '<p style="color: green;">Submitted: ' + name + ' - ' + email + '</p>';
                }
            </script>
        </div>
    </body>
    </html>
    """
    
    # Log before returning response
    print("✅ Returning HTML response to browser")
    logger.info("✅ Successfully generated HTML content")
    print("📊 HTML content length:", len(html_content))
    logger.info("📊 Response prepared with %s characters", len(html_content))
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": html_content
    }
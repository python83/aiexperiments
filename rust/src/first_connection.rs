
//Required Creates
use reqwest::Client;
use tokio;
use serde_json::json;
use std::fs;
use std::io::{self, Read};

// Function to read API key from a file
fn read_api_key_from_file(file_path: &str) -> io::Result<String> {
    let mut file = fs::File::open(file_path)?;
    let mut api_key = String::new();
    file.read_to_string(&mut api_key)?;
    Ok(api_key.trim().to_string()) // Trim to remove extra spaces/newlines
}


// Use async main function with tokio
#[tokio::main]
async fn main() {
   
    // Get the API key
    let api_key_path = ".openaikey"; 
    let api_key = match read_api_key_from_file(api_key_path) {
        Ok(key) => key,
        Err(e) => {
            eprintln!("Failed to read API key file: {}", e);
            return;
        }
    };

    // API Config
    let url = "https://api.openai.com/v1/chat/completions";
    let model = "gpt-4o-mini";

    
    //Prompt for API
    let body = json!({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How are your sales since the DeepSeek Launch?"}
        ]
    });

    //Instantiate a client and make a request
    let client = Client::new();

    match client.post(url)
        .header("Authorization", format!("Bearer {}", api_key))
        .header("Content-Type", "application/json")
        .json(&body)
        .send()
        .await 
    {
        Ok(response) => {
            match response.json::<serde_json::Value>().await {
                Ok(json) => {
                    if let Some(choice) = json["choices"].as_array().and_then(|c| c.first()) {
                        if let Some(response_text) = choice["message"]["content"].as_str() {
                            println!("ChatGPT Response: {}", response_text);
                        } else {
                            println!("Response JSON (unexpected format): {:#?}", json);
                        }
                    } else {
                        println!("Response JSON (unexpected format): {:#?}", json);
                    }
                },
                Err(e) => eprintln!("Failed to parse JSON response: {}", e),
            }
        }
        Err(e) => eprintln!("Request failed: {}", e),
    }
}
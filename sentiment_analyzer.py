from textblob import TextBlob

print("🤖 AI Sentiment Analyzer")
print("Type 'exit' to quit\n")

while True:
    text = input("Enter a sentence: ")
    if text.lower() == 'exit':
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    print(f"Sentiment: {sentiment}\n")

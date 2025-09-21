from textblob import TextBlob

user_input = input("Enter text to analyze: ")
blob = TextBlob(user_input)
sentiment = blob.sentiment
print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

if sentiment.polarity > 0:
    print("The sentiment of the text is Positive.")


elif sentiment.polarity < 0:
    print("The sentiment of the text is Positive.")

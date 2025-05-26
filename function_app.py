import azure.functions as func
import logging
import random

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

MATH_QUOTES = [
    "The essence of mathematics lies in its freedom. - Georg Cantor",
    "Pure mathematics is, in its way, the poetry of logical ideas. - Albert Einstein",
    "Mathematics is the language in which God has written the universe. - Galileo Galilei",
    "The only way to learn mathematics is to do mathematics. - Paul Halmos",
    "Mathematics is the queen of the sciences and arithmetic is the queen of mathematics. - Carl Friedrich Gauss",
    "It is impossible to be a mathematician without being a poet in soul. - Sofia Kovalevskaya",
    "As far as the laws of mathematics refer to reality, they are not certain; and as far as they are certain, they do not refer to reality. - Albert Einstein",
    "Mathematics consists of proving the most obvious thing in the least obvious way. - George Polya",
    "The study of mathematics, like the Nile, begins in minuteness but ends in magnificence. - Charles Caleb Colton",
    "Do not worry about your difficulties in mathematics. I can assure you mine are still greater. - Albert Einstein",
]

@app.route(route="mathquote")
def mathquote_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for a random math quote.')
    random_quote = random.choice(MATH_QUOTES)
    return func.HttpResponse(
        f"Phrase of the Day: \"{random_quote}\"",
        status_code=200
    )

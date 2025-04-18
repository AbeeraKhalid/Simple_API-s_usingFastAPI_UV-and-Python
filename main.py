# Simple API for side hustles and money quotes
from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [

    "Wordpress Development - Create and sell Wordpress themes and plugins!",
    "Graphic Design - Sell your design services to local businesses!",
    "Video Editing - Edit videos for clients and earn a side income!",
    "Social Media Marketing - Manage social media accounts for businesses!",
    "Data Entry - Work from home transcribing and entering data!",
    "Virtual Assistant - Provide administrative support to clients remotely!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Self-Publishing – Write and sell books on Amazon Kindle Direct Publishing (KDP)",
    "Voiceover Work – Offer voiceover services on platforms like Voices.com or Fiverr",
    "Podcasting – Monetize via sponsorships, Patreon, or ads",
    "Music Production – Sell beats on BeatStars or license music on Pond5",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Chatbot Development – Build AI chatbots for businesses",
    "SaaS Business – Develop & sell software as a service (subscription model)",
    "Website Flipping – Improve & resell websites for profit",
    "AI Automation Services – Use AI tools to automate workflows for clients",
    

    
]


money_quotes = [
    
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "A penny saved is a penny earned.",
    "Too many people spend money they haven’t earned to buy things they don’t want to impress people they don’t like.",
    "An investment in knowledge pays the best interest.",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",

]


@app.get("/")
def read_root():
    return {
        "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote"
    }


@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote"""
    return {"money_quote": random.choice(money_quotes)}
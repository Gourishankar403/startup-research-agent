
import random

def get_market_trends(startup_topic: str) -> list:
    fake_trends = {
        "AI": [
            "AI-driven automation across sectors",
            "Concerns over AI-generated misinformation",
            "Investment boom in AI infrastructure startups"
        ],
        "Agritech": [
            "Smart irrigation and water management systems",
            "Drone-based crop monitoring gaining traction",
            "Climate-resilient agriculture startups emerging"
        ],
        "Healthcare": [
            "Telemedicine platforms seeing increased adoption",
            "AI in medical imaging and diagnostics",
            "Health data privacy becoming a core issue"
        ],
        "Fintech": [
            "Rise of embedded finance APIs",
            "Buy Now Pay Later (BNPL) startups cooling down",
            "Increased VC focus on compliance/reg-tech solutions"
        ]
    }

    topic_lower = startup_topic.lower()
    for key in fake_trends:
        if key.lower() in topic_lower:
            return fake_trends[key]

    return random.choice(list(fake_trends.values()))


def get_investor_interest(startup_topic: str) -> dict:
    return {
        "hot_score": round(random.uniform(6.5, 9.5), 2),
        "interested_vcs": random.sample(
            ["Sequoia", "Accel", "Y Combinator", "a16z", "SoftBank", "Lightspeed"],
            3
        ),
        "region_focus": random.choice(["US", "India", "Europe", "Southeast Asia"])
    }


def fetch_dummy_api_data(query: str) -> dict:
    trends = get_market_trends(query)
    investors = get_investor_interest(query)

    return {
        "topic": query,
        "trends": trends,
        "hot_score": investors['hot_score'],
        "top_vcs": investors['interested_vcs'],
        "region": investors['region_focus']
    }

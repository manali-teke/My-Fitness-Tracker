from apps import App
from apps import Mongo

# mongo contains test database details
mongo = Mongo().mongoClient

def insertexercisedata():
    """Define exercise data for all 9 exercises"""
    exercise_data = [
        {
            "email": "email",
            "exercise_id": 1,
            "image": "../static/img/yoga.jpg",
            "video_link": "https://www.youtube.com/watch?v=c8hjhRqIwHE",
            "name": "Yoga for Beginners",
            "description": "New to Yoga? You are at the right place! Learn easy yoga poses to build strength, flexibility, and mental clarity.",
            "href": "yoga"
        },
        {
            "email": "email",
            "exercise_id": 2,
            "image": "../static/img/swim.jpeg",
            "video_link": "https://www.youtube.com/watch?v=oM4sHl1hTEE",
            "name": "Swimming",
            "description": "Swimming is an activity that burns lots of calories, is easy on the joints, supports your weight, builds muscular strength and endurance.",
            "href": "swim"
        },
        {
            "email": "email",
            "exercise_id": 3,
            "image": "../static/img/R31.jpg",
            "video_link": "https://www.youtube.com/watch?v=z6GxFSsx84E",
            "name": "Abs Smash",
            "description": "Whether your goal is a six-pack or just a little more definition around your midsection, we will help get you there!",
            "href": "abbs"
        },
        {
            "email": "email",
            "exercise_id": 4,
            "image": "../static/img/walk.jpg",
            "video_link": "https://www.youtube.com/watch?v=3hlUMzWh8jY",
            "name": "Walk Fitness",
            "description": "Join us to get the best of the walk workouts to burn more calories than a stroll around the park.",
            "href": "walk"
        },
        {
            "email": "email",
            "exercise_id": 5,
            "image": "../static/img/R21.jpg",
            "video_link": "https://www.youtube.com/watch?v=8MAtXXXUvqo",
            "name": "Belly Burner",
            "description": "Join Sasha for a 30-minute no-equipment workout that will work on that stubborn belly fat.",
            "href": "belly"
        },
        {
            "email": "email",
            "exercise_id": 6,
            "image": "../static/img/R22.jpg",
            "video_link": "https://www.youtube.com/watch?v=Qf0L-xtMUjg",
            "name": "Dance Fitness",
            "description": "Shake it off and groove to some fun tracks with Tom and his squad in this dance fitness session!",
            "href": "dance"
        },
        {
            "email": "email",
            "exercise_id": 7,
            "image": "../static/img/R23.jpg",
            "video_link": "https://www.youtube.com/watch?v=Ze7zzMgCdko",
            "name": "HRX Fitness",
            "description": "It's time to push yourself to the limit! Join us for some intense workout sessions.",
            "href": "hrx"
        },
        {
            "email": "email",
            "exercise_id": 8,
            "image": "../static/img/R32.jpg",
            "video_link": "https://www.youtube.com/watch?v=XH7mBWRG9q0",
            "name": "Core Conditioning",
            "description": "Develop core muscle strength that improves posture and contributes to a trimmer appearance.",
            "href": "core"
        },
        {
            "email": "email",
            "exercise_id": 9,
            "image": "../static/img/R11.jpg",
            "video_link": "https://www.youtube.com/watch?v=8IjCdiweJQo",
            "name": "Gym",
            "description": "A collection of Dumbbells workouts by skilled trainers specific to a particular muscle group.",
            "href": "gym"
        }
    ]

    # Connect to MongoDB

    collection = mongo["your_exercise_collection"]

    # Insert exercise data into MongoDB
    for exercise in exercise_data:
        query = {"exercise_id": exercise["exercise_id"]}
        update = {"$set": exercise}
        collection.update_one(query, update, upsert=True)
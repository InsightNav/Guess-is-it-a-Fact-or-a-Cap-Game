import json
import random
from ai_provider import generate

FALLBACK_LIBRARY = [
    {"fact": "A day on Venus is longer than a year on Venus.", "cap": "A day on Mercury is only 45 minutes long."},
    {"fact": "Bananas are technically berries, while strawberries are not.", "cap": "Strawberries are the only fruit with seeds on the inside."},
    {"fact": "Oxford University is older than the Aztec Empire.", "cap": "The Great Wall of China was built to keep out the Romans."},
    {"fact": "Sharks existed before trees did.", "cap": "Dinosaurs were extinct before the first sharks evolved."},
    {"fact": "The longest recorded flight of a chicken is 13 seconds.", "cap": "Chickens can fly continuously for over a minute if trained properly."},

{"fact": "There is a species of jellyfish that is biologically immortal.", "cap": "All jellyfish can regenerate their entire body after dying."},

{"fact": "The inventor of the microwave discovered it when a chocolate bar melted in his pocket.", "cap": "Microwaves were originally invented to dry wet clothes quickly during World War II."},

{"fact": "A group of flamingos is called a 'flamboyance'.", "cap": "A group of owls is called a 'parliamentary circle'."},

{"fact": "Octopuses can taste with their suckers.", "cap": "Octopuses can smell underwater using their tentacles like noses."},

{"fact": "The shortest war in history lasted 38 to 45 minutes.", "cap": "The longest war in history lasted only 3 years due to lack of resources."},

{"fact": "Sea otters hold hands while sleeping so they don’t drift apart.", "cap": "Dolphins sleep in pairs while holding fins to stay synchronized."},

{"fact": "The human brain uses about 20% of the body's total energy.", "cap": "The human brain only becomes active when a person is consciously thinking."},

{"fact": "There are more possible games of chess than atoms in the observable universe.", "cap": "Every possible chess game has already been played at least once in history."},

{"fact": "Some turtles can breathe through their butts.", "cap": "All reptiles can absorb oxygen through their skin when underwater."},

{"fact": "The first computer mouse was made of wood.", "cap": "The first computer mouse used a small trackball made of glass."},

{"fact": "A bolt of lightning is five times hotter than the surface of the sun.", "cap": "Lightning is cooler than lava but appears brighter due to speed."},

{"fact": "Wolves can travel up to 50 miles in a single day.", "cap": "Wolves never travel more than 10 miles from their home territory."},

{"fact": "The heart of a blue whale is so large that a human could swim through its arteries.", "cap": "Blue whales have the fastest heart rate of any animal on Earth."},

{"fact": "Koalas have fingerprints that are almost identical to humans.", "cap": "Koalas can change their fingerprints depending on their diet."},

{"fact": "The Eiffel Tower can be 15 cm taller during hot days.", "cap": "The Eiffel Tower shrinks permanently every winter due to metal fatigue."},

{"fact": "Venus is the only planet that spins clockwise.", "cap": "Mars spins in the opposite direction of Earth every 10 years."},

{"fact": "A snail can sleep for up to three years.", "cap": "Snails must wake up every 24 hours or they die."},

{"fact": "There are more fake flamingos in the world than real ones.", "cap": "Flamingos were once endangered because they could not reproduce in captivity."},

{"fact": "Honeybees can recognize human faces.", "cap": "Bees rely only on smell and cannot process visual patterns."},

{"fact": "The dot over the letter 'i' is called a tittle.", "cap": "The dot over the letter 'i' is called a glyph marker."},

{"fact": "Sharks do not have bones; their skeletons are made of cartilage.", "cap": "Sharks have hollow bones similar to birds to help them float."},

{"fact": "The Moon has moonquakes.", "cap": "The Moon has active volcanoes that erupt once every century."},

{"fact": "A crocodile cannot stick its tongue out.", "cap": "Crocodiles use their tongues to regulate body temperature."},

{"fact": "Butterflies can remember being caterpillars.", "cap": "Butterflies lose all memory during metamorphosis."},

{"fact": "The first alarm clock could only ring at 4 a.m.", "cap": "The first alarm clock could ring at any time but required manual winding every hour."},
]


def get_fact_pair():
    prompt = """
    Give me 2 statements in JSON:
    - one true fact
    - one believable but false statement (about a different topic)

    format:
    {"fact": "...", "cap": "..."}
    """

    try:
        raw = generate(prompt).strip()

        if "```" in raw:
            raw = raw.split("```")[1].strip()

        data = json.loads(raw)
        return data["fact"], data["cap"]

    except Exception:
        # fallback for api if api fails
        choice = random.choice(FALLBACK_LIBRARY)
        return choice["fact"], choice["cap"]
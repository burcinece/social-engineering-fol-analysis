import csv

def load_facts(path):
    facts = set()
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            m = row["MessageID"]
            facts.add(("Message", m))
            if row["Channel"] == "Email":
                facts.add(("Email", m))
            if row["Channel"] == "SMS":
                facts.add(("SMS", m))
            if row["Channel"] == "VoiceTranscript":
                facts.add(("Voice", m))
            if row["SenderKnown"] == "0":
                facts.add(("SenderUnknown", m))
            if row["DomainMatch"] == "0":
                facts.add(("DomainMismatch", m))
            if row["HasLink"] == "1":
                facts.add(("HasLink", m))
            if row["RequestsCredential"] == "1":
                facts.add(("RequestsCredential", m))
            if row["RequestsPayment"] == "1":
                facts.add(("RequestsPayment", m))
            if row["Urgency"] == "1":
                facts.add(("Urgent", m))
            if row["AuthorityClaim"] == "1":
                facts.add(("AuthorityClaim", m))
            if row["Attachment"] == "1":
                facts.add(("Attachment", m))
            if row["MacroRisk"] == "1":
                facts.add(("MacroRisk", m))
            if row["PriorThread"] == "1":
                facts.add(("PriorThread", m))
    return facts

RULES = [
    ("Suspicious", [("SenderUnknown",), ("HasLink",)]),
    ("Suspicious", [("DomainMismatch",)]),
    ("Suspicious", [("Urgent",), ("RequestsCredential",)]),
    ("Suspicious", [("Urgent",), ("RequestsPayment",)]),
    ("PhishingRisk", [("Email",), ("Suspicious",), ("HasLink",)]),
    ("SmishingRisk", [("SMS",), ("Suspicious",), ("HasLink",)]),
    ("VishingRisk", [("Voice",), ("Suspicious",), ("AuthorityClaim",)]),
    ("HighRisk", [("RequestsCredential",), ("DomainMismatch",)]),
    ("HighRisk", [("RequestsPayment",), ("Urgent",), ("SenderUnknown",)]),
    ("HighRisk", [("HasAttachment",), ("MacroRisk",)]),
    ("NeedsHumanReview", [("HighRisk",)]),
    ("NeedsHumanReview", [("PhishingRisk",), ("RequestsCredential",)]),
    ("NeedsHumanReview", [("SmishingRisk",), ("RequestsPayment",)]),
    ("NeedsHumanReview", [("VishingRisk",), ("RequestsCredential",)]),
    ("Safe", [("HasLink",)]),
    ("HighRisk", [("Attachment",)]),
    ("SafeMessage", [("PriorThread",)]),
    ("Suspicious", [("NeedsHumanReview",)]),
    ("NeedsHumanReview", [("Suspicious",)]),
]

def entities(facts):
    return set(f[1] for f in facts)

def forward_chain(facts, rules):
    changed = True
    while changed:
        changed = False
        for head, body in rules:
            for e in entities(facts):
                if all((b[0], e) in facts for b in body):
                    fact = (head, e)
                    if fact not in facts:
                        facts.add(fact)
                        changed = True
    return facts

def classify(facts, message_id):
    labels = set(p for p, e in facts if e == message_id)
    if "NeedsHumanReview" in labels:
        return "NeedsHumanReview"
    if "PhishingRisk" in labels:
        return "PhishingRisk"
    if "SmishingRisk" in labels:
        return "SmishingRisk"
    if "VishingRisk" in labels:
        return "VishingRisk"
    if "Safe" in labels:
        return "Safe"
    return "Suspicious"

def backward_chain(query, facts, rules):
    if query in facts:
        return True
    for head, body in rules:
        if head != query[0]:
            continue
        e = query[1]
        if all(backward_chain((b[0], e), facts, rules) for b in body):
            return True
    return False

if __name__ == "__main__":
    facts = load_facts("messages.csv")
    facts = forward_chain(facts, RULES)
    for m in sorted(entities(facts)):
        print(m, classify(facts, m))
    print(backward_chain(("PhishingRisk", "M001"), facts, RULES))

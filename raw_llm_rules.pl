Suspicious(x) :- SenderUnknown(x), HasLink(x).
Suspicious(x) :- DomainMismatch(x).
Suspicious(x) :- Urgent(x), RequestsCredential(x).
Suspicious(x) :- Urgent(x), RequestsPayment(x).

PhishingRisk(x) :- Email(x), Suspicious(x), HasLink(x).
SmishingRisk(x) :- SMS(x), Suspicious(x), HasLink(x).
VishingRisk(x) :- Voice(x), Suspicious(x), AuthorityClaim(x).

HighRisk(x) :- RequestsCredential(x), DomainMismatch(x).
HighRisk(x) :- RequestsPayment(x), Urgent(x), SenderUnknown(x).
HighRisk(x) :- HasAttachment(x), MacroRisk(x).

NeedsHumanReview(x) :- HighRisk(x).
NeedsHumanReview(x) :- PhishingRisk(x), RequestsCredential(x).
NeedsHumanReview(x) :- SmishingRisk(x), RequestsPayment(x).
NeedsHumanReview(x) :- VishingRisk(x), RequestsCredential(x).

Safe(x) :- HasLink(x).
HighRisk(x) :- Attachment(x).
SafeMessage(x) :- PriorThread(x).
Suspicious(x) :- NeedsHumanReview(x).
NeedsHumanReview(x) :- Suspicious(x).

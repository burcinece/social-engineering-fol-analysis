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

HighRiskSocialEngineering(x) :- HighRisk(x), RequestsCredential(x), RequestsPayment(x).
HighRiskSocialEngineering(x) :- PhishingRisk(x), SmishingRisk(x).
HighRiskSocialEngineering(x) :- VishingRisk(x), HighRisk(x).

UnknownRisk(x) :- Message(x).

Safe(x) :- PriorThread(x), Stratum1_Not_RequestsCredential(x), Stratum1_Not_RequestsPayment(x), Stratum1_Not_Suspicious(x).
NeedsHumanReview(x) :- UnknownRisk(x), Stratum1_Not_Suspicious(x), Stratum1_Not_Safe(x).

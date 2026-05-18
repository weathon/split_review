- Decision: Accept
- Scores: 6, 6, 8, 8, 8

## Merged Review

### Summary
This paper demonstrates that current LLMs can infer personal attributes (e.g., location, income, sex, age) from user-written text with high accuracy (up to 85% top-1, 95% top-3) at a fraction of human cost (100×) and time (240×). The authors construct a dataset of real Reddit profiles, explore both passive inference and active privacy-invasive chatbot scenarios, and show that common mitigations (text anonymization, model alignment) are ineffective. They release 525 human-labeled synthetic examples to aid future research. Reviewers agree the topic is novel and timely, experiments are comprehensive, and the work surfaces important privacy risks.

### Strengths
- First comprehensive study demonstrating the feasibility of LLM-based inference of personal attributes from text (all reviewers).
- Novel privacy threats beyond memorization, well motivated and timely (R1, R2, R5).
- Thorough experimental setup including difficulty ratings for attributes and anonymisation experiments (R3).
- Release of a dataset of 525 human-labeled synthetic examples to support reproducibility and future work (R2, R3, R4).
- Ineffectiveness of current mitigation methods (anonymization and alignment) clearly shown (R4, R5).
- Paper is well organized and presents the attack in two settings (passive and active) (R5).

### Weaknesses
- **Reproducibility concerns:** The exact creation process of the synthetic dataset is not clearly described in the main text, and the appendix does not make reproduction obvious (R1, R3). Results on synthetic examples are not released, hindering future comparisons (R3).
- **Ground truth labeling procedure is insufficient:** Only one human label per profile; no mention of aggregation or inter-annotator agreement. Example: labeling age from “I remember watching the moon landing in 1959” as 70 years is ambiguous without multiple labels (R1, R4). Statistical significance is not established (R4).
- **Human baseline may be weak:** Few humans were tasked with attribute identification using web search with little training; the reported human performance likely underestimates best possible human accuracy (R1).
- **Missing justification for metric choice:** For attributes like age, using accuracy (e.g., within an error tolerance) is not clearly justified; MSE would be more appropriate (R2).
- **Concerns about memorization vs. inference:** The paper controls for memorization only on long comments; it is unclear how much performance stems from memorization of the ACS data or Reddit content (R3). Subreddit prediction performance could further test this (R3).
- **No IRB approval mentioned** for collecting Reddit data containing sensitive attributes (R2).
- **Claim of de-anonymization is a stretch:** The paper does not show how inferred attributes can actually be cross-referenced with public databases to re-identify users; making the threat practical requires additional work (R1).
- **Adversarial interaction attack is brittle:** Users could thwart the coercion attempt via prompt injection; given current LLM brittleness, reliability of such attacks is unclear (R1).
- **Defenses and utility trade-off not addressed:** Anonymization removes utility from shared posts; the paper does not discuss whether defending against inference is desirable given the utility cost (R1).
- **Lack of analysis on correlation among recovered attributes:** Further analysis of how recovery of different PII attributes correlates would strengthen the work (R5).
- **Missing baseline in Figure 25:** It is unclear what the baseline for that figure is (R3).
- **Cost/time numbers need more explanation:** The claimed 85% top-1, 95.8% top-3 accuracy at 100× cost and 240× time savings require more detailed justification (R4).
- **Minor typos:** “Mititgations” → “Mitigations”, “exampels” → “examples” (R2).
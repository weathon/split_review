## Human Reviewer 1

### Summary
This paper introduces RedSage, an open-source cybersecurity-oriented LLM trained via domain-aware continual pretraining and agentic post-training augmentation. This work also proposes RedSage-Bench, a 30K-question benchmark spanning a diverse range of tasks. Authors of this paper claim the model outperforms state-of-the-art specialized baselines on both cybersecurity benchmarks and general LLM tasks, demonstrating that cybersecurity specialization can enhance both domain-specific and general reasoning.

### Strengths
Clear presentation: This work integrates all stages (CPT, SFT, DPO) with substantial data at each phase, which is clearly shown in Fig. 1. Readers can have a very straightforward view on how RedSage was trained on the dataset selected.

Comprehensive Training data coverage: The integration of CyberFineWeb, curated RedSage-Seed, and agentic augmentation provides strong coverage across cybersecurity subfields.

Proposed New Benchmark: What I am interested in is that this work expands prior benchmarks by incorporating tool proficiency and qualitative evaluation, from reviewer’s point of view, this innovation can close a key gap in cybersecurity LLM assessment.

### Weaknesses
May need computational cost analysis: While "compute constraints" are briefly mentioned in page 4 (CyberFineWeb section), there's no breakdown of training time, GPU-hours, or carbon footprint across stages. Adding some analysis on computational cost would help readers to form a general impression on the scale of RedSage training process.

Limited human validation: One of my concern on this work is the data part is heavily reliance on LLM-based verification, which could introduce subtle self-reinforcing biases.

Teacher model (verifier) analysis: Augmentation uses only Llama-3.3-70B and Qwen2.5-72B. Analysis on teacher model can make this paper more solid, such as examining sensitivity to teacher model choice, temperature settings, or comparison with smaller/different teacher models.

Minor issue: Font size on Fig. 3 and Fig. 5 can be larger which I felt difficulty to read

### Questions
As mentioned in the weakness, how do you ensure LLM-generated augmentation does not reinforce factual errors or tool misuse patterns?

How would RedSage perform in interactive cybersecurity reasoning task such as CTF agentic settings on benchmarks like CyBench?

Does the author consider data contamination for the proposed datasets and benchmark?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper presents RedSage, a cybersecurity-focused LLM that is trained with curated pre-training and post-training for cybersecurity knowledge. It presents an elaborate cybersecurity data curation pipeline that uses LLMs for isolating cybersecurity relevant data and augmenting multi-turn conversational data for post-training. The results demonstrate how both pre-training and post-training can help improve performance on cybersecurity tasks.

### Strengths
- The paper clearly demonstrates that cybersecurity curated pre- and post-training improves performance significantly without catastrophic forgetting of general knowledge
- The cybersecurity-specific curated dataset is incredibly useful for future training tasks

### Weaknesses
- The method for open-ended Q&A evaluation is not adequately described. Line 317 mentions "prefix exact match or regex matching" and points to Appendix C.1 however neither the text nor the appendix provide sufficient details or references to clearly understand this evaluation.
- The method for generating the instruction-tuned variant is not explained or referenced. A diagramatic view of how each of the variants was derived would be helpful.

### Questions
- Why is there a large imbalance between MCQ and open-ended Q&A (30K vs 240)? Is it because of human verification of open-ended benchmark? Please provide details of the human verification.
- Some estimates of training time would help future research aiming to replicate this work
- Were other LLMs tried for the agentic augmentation and why were Llama-3.3-70B and Qwen2.5-72B chosen?
- It would be interesting to see how RedSage fairs against models of higher size and commercial models atleast on the general benchmarks. For instance, RedSage-8B-DPO catches up with GPT4 performance on CTIBench-MCQ.

### Soundness
3

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper curates a corpus of data (11.8B tokens) by filtering FineWeb and perform continued pre-training from Qwen3-8B-Base. The resulting models improve cybersecurity multiple-choice benchmarks. Along the way, the authors also introduce a new benchmark, RedSage-Bench.

### Strengths
The paper is well-motivated: to improve a domain-specific capability (cybersecurity), go and curate data for it and fine-tune an existing model.
The paper is fairly well-written and easy to follow.

### Weaknesses
There is not really any methodological novelty, given this is similar to other methods like FineWeb-Edu.
I would have liked to see evaluation of larger models (at least 32B) to see how well the methodology transfers to stronger models (one might worry that the gap will shrink).
It would also be good to get a closed model (e.g., GPT-5 or Claude) to get a ceiling for the new benchmark.
The abstract claims that the fine-tuned model improves on OpenLLM leaderboard tasks, but looking at Table 6, it seems like except on GSM8K, the RedSage is worse as would be expected.

### Questions
How were the labels for the ModernBERT-base clasisifer obtained? Were there an LLMs that were used?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3
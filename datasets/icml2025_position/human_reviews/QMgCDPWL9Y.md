## Human Reviewer 1

### Questions
See strengths and weaknesses

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Questions
Training details for the RL experiments?
- Give more details to how the Go training is conducted. What data is pretrained on ? How is RL conducted? At least one paragraph would be nice
- Again, give more details for the SFT and RL experiments for the orthogonal experiments. what RL algorithm?

### Rating
5

### Confidence
4

---

## Human Reviewer 3

### Questions
1. The experimental validation largely relies on synthetic tasks and esoteric programming languages. Could the authors elaborate on how these results are expected to generalize to more complex, real-world reasoning and decision-making tasks? What evidence do the authors have (or plan to collect) that supports the applicability of the authors' approach beyond controlled experimental settings?
2. Integrating RL directly into the pretraining phase is a bold proposal, but it raises concerns about computational feasibility at scale. How do the authors plan to address the potential exponential increase in computational cost, especially when training on massive, web-scale datasets typical for state-of-the-art LLMs?
3. The idea of decoupling memory from reasoning is central to the authors' position, yet the paper lacks sufficient architectural details. Could the authors provide a more concrete description—such as diagrams, pseudocode, or specific implementation strategies—that clarifies how the proposed hybrid memory-reasoning system will function and be stabilized during training?
4. While the analogy with AlphaGo versus AlphaZero is compelling, planning and reasoning in natural language domains differ substantially from board game strategies. How do the authors justify this analogy, and what specific aspects of LLM reasoning do the authors believe directly correlate with the exploration benefits observed in RL systems like AlphaZero?

### Rating
3

### Confidence
4

---

## Human Reviewer 4

### Questions
How do we train with RL from the start? What kind of reward signals would guide an LLM without human-labeled data?
What do these artificial environments look like? Are they structured like programming tasks, games, or something else? How do we ensure skills transfer to real-world language tasks?
How do we prevent new reasoning traps? Could models still get stuck in loops, just in different ways?
What’s the computational cost? RL is expensive—how can we make this training method scalable?
How do we evaluate success? If reasoning is learned through search, what benchmarks prove it’s actually improving?
What about safety? How do we ensure models exploring freely don’t generate harmful or biased outputs?

### Rating
4

### Confidence
4
# Modeling Beyond MOS: Quality Assessment Models Must Integrate Context, Reasoning, and Multimodality

- Decision: Reject
- Scores: 4, 5, 6

## Abstract
This position paper argues that Mean Opinion Score (MOS), while historically foundational, is no longer sufficient as the sole supervisory signal for multimedia quality assessment models. MOS reduces rich, context-sensitive human judgments to a single scalar, obscuring semantic failures, user intent, and the rationale behind quality decisions. We contend that modern quality assessment models must integrate three interdependent capabilities: (1) context-awareness, to adapt evaluations to task-specific goals and viewing conditions; (2) reasoning, to produce interpretable, evidence-grounded justifications for quality judgments; and (3) multimodality, to align perceptual and semantic cues using vision–language models. We critique the limitations of current MOS-centric benchmarks and propose a roadmap for reform: richer datasets with contextual metadata and expert rationales, and new evaluation metrics that assess semantic alignment, reasoning fidelity, and contextual sensitivity. By reframing quality assessment as a contextual, explainable, and multimodal modeling task, we aim to catalyze a shift toward more robust, human-aligned, and trustworthy evaluation systems.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This position paper critiques the long-standing reliance on the Mean Opinion Score (MOS) as the primary supervisory signal in multimedia quality assessment (MQA). It argues that MOS-based evaluation flattens complex, context-sensitive human judgments into a scalar, obscuring semantic failure, user intent, and interpretability. The authors advocate for a paradigm shift, proposing models that are (1) context-aware, (2) capable of structured reasoning, and (3) multimodal. They outline a roadmap for benchmark and metric reform, suggesting richer datasets, persona-conditioned ratings, rationales, artifact maps, and reasoning-based evaluation metrics. The paper calls for a structured, explainable, and trustworthy approach to quality modeling beyond scalar regression.

### Strengths
Strong and timely critique of entrenched MOS-centric methodology.

Comprehensive breakdown of limitations—semantic collapse, lack of interpretability, brittleness in NR settings, etc.

Clear articulation of three foundational principles (context, reasoning, multimodality).

Practical roadmap including benchmark reforms, data collection pipelines, and evaluation methodologies.

### Weaknesses
While rich in vision, some proposals (e.g., simulation with persona-conditioned agents) lack detailed feasibility analysis.

Certain sections (e.g., multimodal attention fusion) assume significant model capabilities without clear limitations discussed.

Empirical validation is absent—though understandable for a position paper, references to pilot experiments or datasets could increase concreteness.

Limited discussion on how the proposed structured outputs might be evaluated quantitatively beyond existing CoT metrics.

### Questions
Could you elaborate on how reasoning metrics (like coherence, grounding, etc.) could be standardized across diverse quality tasks (e.g., aesthetic vs. clinical)?

How would proposed structured outputs scale to real-time applications with tight latency constraints (e.g., video streaming)?

What are the risks of overfitting to persona biases in simulation-based evaluation?

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This position paper argues that Mean Opinion Score (MOS)—the dominant scalar supervision signal for multimedia quality assessment (MQA)—is insufficient for modern use cases. The authors propose a shift toward context-aware, reasoning-capable, and multimodal quality models that go beyond scalar regression. They advocate for structured outputs (e.g., rationale, attention, artifact maps) and reforms to benchmark design. The paper is timely and well-motivated, offering a clear roadmap and unifying recent trends (VLMs, CoT reasoning, RLHF) under a coherent narrative.

### Strengths
1. Well-scoped problem: The authors clearly articulate the limitations of MOS supervision, including lack of context, explainability, uncertainty modeling, and semantic alignment.

2. Timely and visionary: The proposal aligns with current trends in VLMs, LLMs, explainability, and human-centric evaluation. It serves as a call-to-action for the next generation of evaluation frameworks.

3. Detailed roadmap: The paper includes concrete proposals for benchmark reform: persona conditioning, reasoning metrics, multi-perspective annotation, and structured outputs.

4. Broad impact: The ideas generalize across image, video, audio, and aesthetic quality assessment, touching domains such as healthcare, autonomous driving, and content creation.

### Weaknesses
1. Lack of concrete implementation or MVP (Minimum Viable Prototype)
The paper would be significantly stronger with a minimal system demo (e.g., small-scale structured-output model trained with reasoning and context). Currently, the claims are speculative.

2. Evaluation metrics are underspecified
The authors advocate for evaluating reasoning, alignment, and context-sensitivity, but no concrete metrics or protocols are defined (e.g., how to score attention-text-artifact alignment or rationale factuality). A table summarizing proposed metrics vs traditional ones would be helpful.

3. No small-scale user study or data annotation experiment
Since the authors emphasize personas and multi-perspective annotations, it would be useful to report the cost, inter-rater variance, or feasibility of collecting such data on a small scale (e.g., 200 samples with rationales and semantic error tags).

4. Computational cost & practical concerns under-addressed
Though briefly mentioned in rebuttal (e.g., MoE/adapters), the paper lacks a detailed cost-benefit analysis or deployment tradeoff discussion (e.g., tiered pipelines for low-risk vs. high-risk settings).

### Questions
1. Can the authors provide a small-scale prototype that demonstrates structured outputs (e.g., score, rationale, attention, artifact mask) on ~100 examples?
2. Can the authors define concrete evaluation metrics (e.g., alignment consistency, rationale grounding, uncertainty calibration) to support their proposed modeling paradigm?
4.Would the paper benefit from a figure illustrating the proposed evaluation pipeline and contrasting it with the traditional MOS-only approach?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues that using simple average scores (MOS) to train AI quality assessment models is fundamentally broken. Instead, they want models that can explain their reasoning, adapt to different contexts (like medical vs social media), and handle multiple types of input.

The problem: Current models just learn to predict average human ratings, so they miss semantic failures (like AI-generated images with extra limbs that look "sharp" but are obviously wrong) and can't explain why something is low quality.

Their solution: Train models to output structured explanations, context-aware scores, and visual attention maps instead of just numbers.

### Strengths
1. The paper is well written and targets an important problem on quality assesment - This could be important given the surge in Video generation , image generation etc. 

2. The argument that inter-rater disagreement contains valuable information rather than being noise is compelling and potentially underexplored in the quality assessment literature.

3. The authors provide concrete data (e.g., "standard deviations range from 0.6 to 1.5," "variance differences exceeding 1.0," "inter-subject variance up to 20 points") from multiple datasets, demonstrating thorough literature review.

4. The authors move from pure critique to proposing concrete modeling principles (context-awareness, reasoning, multimodality). This is what a position paper should do and they do that very well. Seeems like a good technical direction, it could elicit some spark in the community.

### Weaknesses
1. While the proposed framework is a step in the proposed position, it's essentially a combination of existing techniques (CoT, vision-language models, attention mechanisms, meta-learning). The novelty lies in applying them to quality assessment, not in the techniques themselves.

2. How exactly would you train such a system which is proposed in the paper? What's the loss function? How do you ensure the different alignment objectives don't conflict? These crucial details are missing.

3. The proposed framework seems computationally expensive (multiple modalities, reasoning chains, attention mechanisms) but there's no discussion of practical constraints.

4. While the infrastructure proposals are detailed, they're largely engineering solutions rather than algorithmic innovations. I am not sure if thats what the NuerIPS community expects. 

5. The paper proposes extensive reforms but provides no pilot studies, proof-of-concept experiments, or even small-scale validation of these ideas. The claims about efficiency gains and reliability improvements are borrowed from other work.

### Questions
Why should these specific reforms work?  this is what i am still missing . can the authors help answer this question. 

Thanks for the good work. Looking forward the discussion during rebuttal. Thanks

### Presentation
3

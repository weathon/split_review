# The Two-Hop Curse: LLMs trained on A→B, B→C fail to learn A→C

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
While LLMs excel at answering multi-hop questions like “Who is the spouse of the performer of Imagine?” by thinking out loud (chain-of-thought), they perform surprisingly poorly when required to reason in their latent space and answer without chain-of-thought. This observation was previously referred to as the compositionality gap, implying that although language models are less reliable at two-hop latent reasoning, they still perform it sometimes. In this paper, we introduce a controlled setting for investigating the compositionality gap. We run a series of experiments finetuning a large language model (Llama-3-8B-Instruct) on synthetic facts expressed in English. We attempt to elicit two-hop reasoning in three ways: (i) fine-tune on a data mixture designed to incentivize two-hop reasoning, (ii) force facts to be stored in layers in the correct order, and (iii) use an auxiliary loss to provide activation-level supervision for two-hop reasoning. We show that LLaMA 3 8B successfully learns to answer two-hop questions about synthetic facts using CoT, but completely fails without CoT, achieving chance-level accuracy and chance-level test loss. Failures of LLMs in our controlled setting cast doubt on the purported ability of present LLMs to perform multihop latent reasoning and lead us to conjecture that, rather than a reasoning gap, current language models might exhibit a two-hop reasoning curse — a complete lack of ability rather than a relative weakness. This is the Two-Hop Curse.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the compositionality gap in LLMs: why do LLMs fail to answer two hop questions directly but can do so with CoT.

### Strengths
This paper studies an interesting problem, the compositionality gap, although with relatively shallow experiments (restricted to one model on a simple synthetic dataset). It tries different approaches to address this, although the motivation for the auxiliary objectives need to be strengthened (currently feels very ad-hoc).

### Weaknesses
1. This work is quite incremental given the existing literature on compositionality gap (Press et al, 2023).
2. Further the experiment is carried out only in a very simple synthetic domain.
3. The experiments are performed using only one model, so this and the previous points brings the generalizability of this study into question.
4. The motivation for this work needs to be clarified, as the LLMs do perfectly well with CoT.
5. Several phrases used without proper definitions of them: "two-hop circuitry", "Goldilocks zone"

### Questions
What is the motivation behind this study given CoT does well?
Why is the study restricted to only a simple synthetic dataset and only one model?
What is the key differentiating factors between this work and the several prior works on compositionality gap of LLMs?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The author proposes a series of experiments to explore the "two-hop curse" observed in large language models (LLMs). Using atomic data in different configurations, they select two types of two-hop data: one without chain-of-thought (CoT) reasoning and one with CoT reasoning, to fine-tune the Llama3-8B model. This approach effectively allows control over the data that influences the LLM's parameters. The author finds that adding two-hop CoT data increases accuracy for two-hop questions; however, it still fails to improve performance on two-hop questions without CoT. Additionally, two intervention tests were conducted to assess their impact, but both showed minimal effect. Overall, this paper provides a detailed analysis of the phenomenon known as the "compositionality gap."

### Strengths
- The study employs fine-grained control over the training data and conducts a series of experiments to meticulously examine the compositionality gap in large language models.

### Weaknesses
This is an analytical paper that conducts various experiments and research on a specific phenomenon. However, it does not present particularly impressive conclusions or unique perspectives. The results obtained from intervention2 and intervention3 are not positive, but we should see more reasons that lead to the occurrence of the phenomenon in the main papaer, rather than this "process of elimination." In addition, the author's motivations and explanations for their interventions are not convincing.

### Questions
- Intervention 2: We observe that one-hop accuracy from layer-selective experiments also declined. Could you elaborate on how this affects the decrease in two-hop reasoning performance?

- Additionally, could you explain your motivation for choosing these two specific interventions over other possible options?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work sets out to investigate the compositional reasoning gap of LLMs. The authors design three different approaches to elicit two-hop reasoning of pre-trained LLaMA-3-8B: fine-tuning on mixed data, staged fine-tuning to force the first-hop facts and the second-hop facts to be stored in different layers and leveraging additional supervision signal to encourage the emerge of bridge entity in the middle layers. They offer a converged conclusion: LLaMA-3-8B completely fails to learn to generalize to compositional reasoning cases without chain-of-thought prompting.

### Strengths
1. The presentation, logic-flow of the paper is good. The paper is overall well writen and easy-to-follow.
2. The topic of the work "the limitations of the compositional reasoning in large language models" is interesting and important as well.
3. The experiments designed in the paper are quite multi-faceted, offering some insightful results to readers.

### Weaknesses
1. Though the experiments presented in the paper, it only explore a few settings (fine-tuning on mixed data, staged fine-tuning to force the first-hop facts and the second-hop facts to be stored in different layers and leveraging additional supervision signal to encourage the emerge of bridge entity in the middle layers). Negative results on such settings might be insufficient to claim that LLMs exhibit a near-complete failure of two-hop latent reasoning.
2. As the authors stated in the Limitation section, the paper mainly focus on making LLMs acquire knowledge via fine-tuning, different from pre-training (where typically we do). This may weaken the insights brought by the work.
3. The variation of the data is quite limited: only covering factual knowledge data and only two semantic templates (spouse and birth city), which may prevent the model from learning some general composition skills.

### Questions
1. One of the contributions claim that the experimental setup can alleviate memorization or reasoning short cuts. How do the dataset settings control the memorization or reasoning short cuts? I may overlook some details? Did you use the counter-factual (or virtual) data to conduct the experiments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the limitations of LLMs in performing "two-hop" reasoning in their latent space. The authors create a controlled setup using Llama 3 8B, where they fine-tune the model with three strategies aimed at eliciting two-hop reasoning without CoT: data mixtures that encourage two-hop reasoning, layer-ordering of facts to align with logical steps, and activation-level supervision. Despite these methods, LLMs could not reliably perform two-hop reasoning without CoT, failing to exceed chance-level accuracy. This suggests that LLMs may lack fundamental latent reasoning capabilities, potentially highlighting an intrinsic limitation of current transformer models.

### Strengths
1.The authors address a highly intriguing problem, investigating weaknesses in LLMs and pointing to directions for future optimization.

2.The experimental design minimizes the impact of the model's pre-existing knowledge on the results, thereby increasing the reliability of the conclusions.

### Weaknesses
1. The paper lacks novelty, as previous works, such as arxiv.org/pdf/2406.12775 and arxiv.org/pdf/2402.16837, have already investigated the limitations of LLMs in multi-hop reasoning. The authors should further discuss the distinctions between their study and these prior works.

2. The study identifies the "two-hop curse" phenomenon through experimental analysis but does not delve into the underlying causes of this limitation, nor does it propose any effective methods to alleviate it.

3. The experimental design lacks sufficient depth; the constructed dataset contains only one pattern (“The spouse of e1 is e2. The birth city of e2 is e3”), without covering other relational structures. Additionally, only the Llama 3 8B model is evaluated, leaving open the question of whether larger models or different architectures would also experience the two-hop curse.

4. Several details remain unclear, such as specific hyperparameters for the training setup (e.g., learning rate, warmup ratio), and some methods need further theoretical explanation, particularly Inventions 2 and 3. There is approximately a page and a half of space that could be used to expand on these aspects.

Minor Issues:

1. The color differentiation in Figure 1 is minimal, making it difficult to discern details.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

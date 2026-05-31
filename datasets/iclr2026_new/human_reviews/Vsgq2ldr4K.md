## Human Reviewer 1

### Summary
a new inference scaling method that can match the RL performance by spending cost during decoding, but does not require training, verifiers, datasets.

### Strengths
- the method is conceptually simple and straightforward
- the method does not require any training, data or verifier, and is entirely formed by the base model's own distribution

### Weaknesses
- need to pay cost for each sample, and if not paying for any inference scaling cost degenerates to sampling from p.
- the evaluated benchmarks are rather older. do we expect the method to be still tractable with harder datasets that require longer CoT lengths? at least evaluate AIME25 or better HMMT25/BRUMO25, which are common math reasoning benchmarks to be tested on

### Questions
- why was there a decrease in performance when increasing the MCMC steps, was this more noisy as high likelihood samples could also be wrong? could be good to provide distributional stats for plot 5 b.
- did you try your method on top of GRPO'd models, what will happen?

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This work investigates how distribution sharpening can improve reasoning without additional training. The authors introduce a simple iterative sampling algorithm that leverages the base model’s own likelihoods to refine generation. Across three different base models and a range of benchmarks, the proposed method achieves competitive performance with alignment-trained models—while requiring no post-training or additional data.

### Strengths
- The paper reframes alignment and reasoning improvement as a distribution-sharpening problem, bridging the gap between post-training RL methods and pure inference-time algorithms.
- The proposed iterative sampling algorithms is simple, straightforward but exceptionally effective.
- The authors conducted solid experiences across 3 base models and several benchmarks to demonstrate the proposed method's effectiveness.

### Weaknesses
- The experiments are only conducted on small models such as Qwen2.5-7B. Experiments on more advanced models and larger models can further solidify the empirical exploration. But it is understandable given the resources in academia.
- The evaluation spans four benchmarks, which, while representative, do not fully capture the diversity of reasoning and generation tasks.

### Questions
- Why does applying GRPO to Phi-3.5-mini-instruct result in performance degradation on two math benchmarks? The authors should further analysis the underlying cause of this phenomenon.

### Soundness
4

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
This paper proposes a training-free method to improve reasoning in large language models (LLMs) by sampling from a sharpened distribution of the base model. Inspired by ideas from Markov chain Monte Carlo (MCMC), the authors introduce an inference-time sampling algorithm that approximates sampling from a power distribution, where higher-likelihood sequences under the base model are exponentially upweighted.

### Strengths
- The paper offers a fresh conceptual lens by interpreting RLVR-based improvements as a form of distribution sharpening, reframing how we think about reasoning emergence in LLMs.
- The authors demonstrate that a simple, training-free algorithm can match or surpass GRPO-trained models across multiple benchmarks and model families.

### Weaknesses
As noted by the authors, the method can only exploit existing capabilities of the base model—it cannot exceed its representational capacity. A deeper discussion or analysis of the top-k ceiling would help contextualize the results.

### Questions
- Have the authors evaluated Power Sampling on open-ended tasks like story writing or dialogue? If not, what properties of reasoning tasks (e.g., verifiability, objective correctness) make sharpening effective?
- Is a higher base model likelihood always desirable? Could overly sharp distributions lead to degenerate or repetitive text, as seen in low-temperature sampling?
- In my own experiments, sharpened sampling does not seem to improve autoregressive image generation. Do the authors believe that *reasoning tasks* uniquely satisfy conditions that make $p^{\alpha}$ beneficial?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
- The paper shows that strong reasoning performance can be achieved from base LLMs without any additional training by changing how we sample from them.
- It introduces a power sampling algorithm that draws from a sharpened distribution $p_{\alpha}(\mathbf{x}) \propto p(\mathbf{x})^\alpha$, emphasizing higher-likelihood reasoning traces.
- The method uses an MCMC-style resampling process to approximate sampling from this distribution efficiently at inference time.
- Across several benchmarks such as MATH500, HumanEval, and GPQA, this training-free approach matches or surpasses GRPO-based post-training.
- The results suggest that base models already encode strong reasoning abilities, and that better inference-time sampling can unlock them without retraining.

### Strengths
- The method achieves RL-level reasoning performance without any additional training, data, or reward signals.
- It provides a clear theoretical analysis showing why power sampling differs fundamentally from conventional low-temperature sampling.
- The algorithm is simple, mathematically principled, and broadly applicable to existing base language models.
- The work reframes reasoning enhancement as an inference-time sampling problem rather than a post-training or reward-learning problem.

### Weaknesses
- It depends on tuning the power factor, block size, and number of MCMC steps, which may limit plug-and-play usability.
- The algorithm provides no theoretical guarantee of convergence to the true power distribution in large sequence spaces.
- The paper evaluates only single-shot responses and does not test multi-turn reasoning or chain-of-thought extensions.

### Questions
- How can $\alpha$ be selected practically and automatically without extensive tuning?
- Does power sampling remain effective for longer reasoning chains or multi-turn dialogues?
- How does the diversity of outputs change with increasing $\alpha$ and MCMC steps, and is there a risk of collapsing to repetitive or overconfident generations?
- Have you considered evaluating the proposed method on more challenging or diverse reasoning benchmarks such as MMLU?
- Could you provide insights into why $\alpha = 4.0$ consistently works well across tasks?
- Have you considered using tempered transitions within your MCMC framework to improve chain mixing, especially when sampling from highly sharpened distributions for long reasoning sequences?
- In Line 17, Line 46, and more, capabilites -> capabilities
- In Line 356, algorihtms -> algorithms
- The figures use multiple shades of blue that differ only in brightness, making it difficult to distinguish between lines or bars, especially when printed or viewed in grayscale. The authors are encouraged to adopt a more distinguishable color palette.
- Use \citep and \citet appropriately.
- Ensure that the citation formats are consistent, the capitalization is correct, and the reference information is up-to-date.

### Soundness
4

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
4
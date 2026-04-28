# Synthetic Theorem Generation in Lean

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
The application of large language models (LLMs) to theorem proving presents a promising avenue for advancing formal mathematics. Interactive theorem provers, such as Lean, offer a rigorous framework within which these models can assist in or automate proof discovery, grounding their reasoning capabilities in a sound, verifiable formal system. However, the potential of LLMs in this domain is constrained by the limited availability of formal proof corpora for training. To address this limitation, we introduce a synthetic theorem generator capable of producing novel Lean theorems and their corresponding proofs. Our approach employs forward reasoning to synthesize new propositions from premises drawn from existing Lean libraries. We explore candidate reasoning steps using a search strategy that optimizes for diversity of output, apply them in a linear fashion that avoids irrelevant proof steps, and assess their effect by meta-programmatically executing corresponding Lean tactics. These methods enable the generation of an arbitrary number of new theorems and proofs across various mathematical domains, using common Lean proof tactics while ensuring the correctness of generated theorems by construction.  We demonstrate the efficacy of the generated theorems and training data by fine-tuning models on synthetic theorems and evaluating them on the miniF2F-test benchmark. Our results show improvements in theorem-proving capabilities, with accuracy increasing from 37.3% to 38.5% for the Falcon2-11B model trained solely on Mathlib, and from 38.1% to 39.3% for the same model trained on a mix of rich datasets. These improvements highlight the value of our diverse synthetic data in augmenting limited existing corpora of formal proofs, providing complementary information that enhances LLMs' performance on theorem-proving tasks even when combined with other datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a framework for generating synthetic Lean theorems and proofs to supplement the training corpus for neural theorem provers. The main approach involves forward proving, where proof states from existing Lean libraries are transformed using a small set of curated proof tactics and model-selected premises. The effectiveness of this framework has been empirically demonstrated on the miniF2F dataset, with the Falcon2-11B model showing improved performance when fine-tuned on the synthetically augmented Lean Workbook dataset.

### Strengths
- Well-motived objective: augmenting existing formal corpus synthetically is surely of immerse interest, given the limited amount of formal corpus available.
- The paper is relatively well-written and easy to follow, and with good amount of implementation details in the appendix for reproducibility.

### Weaknesses
 - There is a lack of experiments validating the effectiveness of using diverse (synthetic) theorems. Based on my experience, synthetic data augmentation typically provides significant benefits, even when theorems are randomly mutated. A key innovation of this paper is the algorithm depicted in Figure 3, which aims to promote diversity. However, in the subsequent experiments, it seems the authors have not established a robust metric to assess the diversity of the generated theorems or to quantify how this diversity impacts the performance of fine-tuned neural provers.
- As an alternative method for augmenting the formal corpus, it would be beneficial to include more comparisons between autoformalization and the proposed synthetic approach. Does the synthetic approach generate more diverse theorems? With an equal amount of additional corpus from each method, would the synthetic approach yield better performance on the fine-tuned prover? Additionally, what impact might combining these two approaches have on overall performance?

### Questions
- I would appreciate some more elaboration on why the 'have' tactic needs a lemma from the library to introduce a new hypothesis
- It might be interesting to include a qualitative analysis of the additional theorems proven using the synthetic dataset.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to synthesizing new theorems in Lean. It utilizes forward reasoning tactics to construct new theorems based on a collection of existing proof states from the Mathlib library or Lean workbook. Additionally, it incorporates premise selection and proposes innovative search strategies to ensure the diversity and usefulness of the generated theorems. By using these newly generated theorems as complementary training corpus, the resulting theorem proving agent demonstrates an improvement of approximately 1% (3 problems) over the ablated setting.

### Strengths
- Given the current status of formal theorem proving, the need for a method capable of synthesizing theorems across a broad domain in Lean is critical. Therefore, the motivation for this work is compelling, and it represents a significant attempt to address the theorem generation problem in a wide context.

- This paper explores a novel approach to constructing new theorems in Lean. The use of forward reasoning to construct theorems has previously only been applicable in term mode, and I believe this is the first work to introduce this approach in tactic mode.

- The paper introduces several interesting components to ensure that the generated theorems are diverse and useful while eliminating unnecessary steps in the generated proofs.

### Weaknesses
 - The usefulness of these synthesized theorems is a significant concern. The ablation performance using these generated theorems is quite weak, with only 3 additional theorems proven in miniF2F in both settings (M1 and M2). This is notable given that the tokens for the synthesized proofs amount to approximately 1 billion, compared to 208 million tokens in Mathlib.

- (Please correct me if I'm wrong) It appears that the tactics used to develop these forward reasoning steps are limited to a small subset, with only 5 tactics described in lines 296 to 301. Does this imply that the generated theorems will also only employ these 5 tactics? Considering the large variety of backward reasoning tactics available in Lean, generating theorems based solely on this limited subset of forward reasoning tactics could result in a biased set of synthetic data. I assume this is why the performance with these synthetic data is not more prominent.

- The paper is not very well written. Although the logic is easy to follow, the graphs are not particularly illustrative and lack detail. It would be beneficial to include a concrete, illustrative example when describing the method, as this would make the paper much easier to understand.

### Questions
- Is it true that the base tactics used for theorem generation (excluding variants with specific parameters) consist of only five (or a slightly larger number)? Will the final generated theorems be limited to tactics from this set?

- Could you provide some concrete examples of the generated theorems? A detailed process showing how one of these theorems is created would be particularly helpful.

- In lines 73–76, references for "Some" and "Other techniques" should be added.

- In lines 115–116, I believe the references "(An et al., 2024; Polu & Sutskever, 2020; Zombori et al., 2021)" are misplaced. These do not pertain to methods used for generating theorem statements.

### Soundness
3

### Presentation
2

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
This paper presents a synthetic generator to create diverse new theorem and proof data for Lean 4 by forward reasoning and premise selection in existing libraries like Mathlib. By applying the generator to Lean Mathlib and Lean Workbook dataset, the authors demonstrate improvements in theorem-proving performance, with a fine-tuned Falcon2-11B model showing increased accuracy from 38.1% to 39.3% on the miniF2F benchmark.

### Strengths
1. The paper is logically structured and comprehensively explains the generator’s architecture, from premise selection to proof synthesis search and minimization. The methodology for generating synthetic theorems through forward reasoning is well-justified. 
2. The approach’s reliance on premise selection using the LeanDojo ReProver model ensures theorems remain relevant and mathematically grounded, leading to meaningful performance gains on the miniF2F benchmark. 
3. This paper significantly advances synthetic data generation for theorem proving by moving beyond simple mutation to generate genuinely new theorems and mitigate the data scarcity issue in formal theorem proving. The use of forward reasoning allows for the production of diverse, novel theorems, which may expand formal datasets in ways that mutation alone may not achieve.

### Weaknesses
1. Marginal Improvement in Benchmark Performance: Despite generating millions of synthetic theorems and proofs, the fine-tuning of these theorems leads to only a modest improvement in miniF2F performance for the Falcon2-11B model trained on a mixed dataset (from 38.1% to 39.3%). This improvement is notably lower than state-of-the-art approaches such as DeepSeekProver v1.5 and InternLM Prover v2.5, which achieve over 60% on miniF2F dataset. This raises concerns regarding the quality and utility of the generated theorems for practical theorem proving. The small increase suggests that the synthetic data, while syntactically correct, may not be semantically rich or diverse enough to significantly enhance the model's reasoning capabilities on challenging benchmark problems. The limited improvement could also indicate that the generated theorems do not target the specific weaknesses of the model, or that the model architecture itself is a bottleneck.
2. Lack of Quality Metrics for Synthetic Theorems: The paper does not provide specific metrics or validation methods to assess the quality or relevance of the generated synthetic theorems. The absence of such metrics makes it difficult to determine whether the synthetic data aligns well with mathematically significant problems or contains inherent limitations affecting model performance. It is unclear if the generated theorems are merely variations of existing ones or if they introduce genuinely new mathematical insights. Without metrics to evaluate the novelty, complexity, and difficulty of the generated theorems, it's hard to gauge the true value of the synthetic dataset. For example, metrics could include the average number of steps in the proof, the depth of the dependency graph of the proof, or the number of unique tactics used.
3. Computational Requirements: The generation process requires significant computational resources (60 * 36 vCPU for 24 hours), even if the search depth is not very high (10). It may potentially limit accessibility for broader use. The high computational cost raises concerns about the practicality of the approach for researchers with limited resources. The paper should provide a more detailed analysis of the computational bottlenecks and explore potential optimizations to reduce the resource requirements. For example, the authors could investigate the impact of reducing the search depth or using more efficient data structures.

### Questions
1. Given the modest improvement in miniF2F accuracy, are there any metrics or quality checks in place to evaluate the significance and validity of the generated theorems and proofs beyond their correctness by construction?
2. Which specific theorems in miniF2F were newly proved by the Falcon2-11B model fine-tuned with synthetic data? These examples could help clarify the types of problems that benefit from synthetic training.
3. Could this approach be modified or enhanced to better align with the needs of SOTA theorem-proving systems, potentially addressing the disparity in miniF2F performance compared to SOTA models? Is there any specific reason to use Falcon2-11B compared to other models?
4. In Appendix B, you assumed a TacticsFor function in Algorithm A that returns a set of applicable theorems at a proof state. How is this function implemented? Is it time-consuming since it may require to iterate over all potential theorems and variable assignments?
[1] Xin, Huajian, et al. "DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search." arXiv preprint arXiv:2408.08152 (2024).
[2] Ying, Huaiyuan, et al. "Lean Workbook: A large-scale Lean problem set formalized from natural language math problems." arXiv preprint arXiv:2406.03847 (2024).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents an approach for generating synthetic formal theorems and their corresponding proofs by leveraging existing libraries through forward reasoning. Specifically, it focuses on modifying a given proof state by combining premise selection with a set of predefined tactics (e.g., `rewrite`, `simp_arith`). The method retrieves relevant lemmas and applies these tactics to generate new proof states. Additionally, the paper introduces several optimizations to enhance the diversity and quality of the generated theorems. These include a search algorithm to produce a broader variety of theorems within the same computational budget and the use of tactics like `omega` or `aesop` for proof minimization. By utilizing the Mathlib and Lean Workbook datasets, the approach can synthesize up to a million new theorems, expanding existing datasets. Experiments on miniF2F show that fine-tuning LLMs on this extended dataset leads to improved performance compared to fine-tuning on the original dataset alone.

### Strengths
> The paper is well-written and easy to follow.

> The proposed method is intuitive and is able to generate millions of new theorems from existing libraries. This addresses, to some extent, the critical challenge of data scarcity in formal theorem proving.

> The experiments show that fine-tuning on the extended dataset could lead to improved performance.

### Weaknesses
 > Lack of Technical Novelty in Synthetic Theorem Generation

The approach of using forward reasoning for generating synthetic theorems and proofs is not particularly novel, as it has been widely explored in previous work. While this paper distinguishes itself by generating theorems from existing libraries rather than basic axioms in Lean, it still follows a similar, well-established pipeline. The core idea of iteratively applying tactics to a proof state to derive new theorems is not a new concept, and the paper does not introduce significant innovations in this aspect of the methodology.

> Potential Limited Diversity and Difficulty of Generated Theorems

The proposed method utilizes only five tactics applied in a linear fashion for synthetic generation, which may limit the variety of theorems it produces. This approach risks generating theorems that are structurally similar and lack the complexity and diversity seen in human-written proofs. The limited set of tactics, such as `rewrite`, `simp_arith`, and `omega`, may not be sufficient to explore the full range of mathematical reasoning. As a result, the generated theorems tend to lack both diversity and complexity, particularly when compared to those written by humans. Additionally, the absence of examples of the generated theorems and their proofs in the paper makes it difficult to accurately evaluate the quality and difficulty of the generated datasets.

> Marginal Experimental Results

Despite the synthetic dataset being 10 times larger than the original (2B vs. 208M), the performance improvement is modest (e.g., the number of proved theorems only rises from 91 to 94, or 93 to 96). The paper also lacks an ablation study to evaluate the quality of the synthetic data or explain which theorems are newly proved. It’s unclear whether the additional proofs are due to the five tactics (or `omega`), or just the randomness of the experiments. The small performance gains raise concerns about the practical utility of the generated dataset. It is not clear if the improvement is statistically significant, and the lack of detailed analysis makes it difficult to ascertain the true value of the synthetic data.

Nit: Figure 1, which explains basic background information, feels unnecessary. It would be more useful to include examples of the synthetic datasets or newly proved theorems in the miniF2F benchmark after fine-tuning on the extended datasets. Additionally, in Table 1, the label for the number of random premises seems to be fractional, but it’s listed as a percentage (%) in the row title, which could be misleading.

### Questions
> Could you conduct experiments or analysis to evaluate the quality of the synthetic datasets? For instance, how does the LLM perform when fine-tuned solely on the synthetic data? Additionally, could you compare the performance of a model fine-tuned on an equivalent-sized synthetic datasets to one trained on the real-world datasets?

> Could you also provide examples or newly proved theorems from the miniF2F-test, along with the specific tactics the model used to prove them? Additionally, do the theorems proved by the model fine-tuned on the extended datasets (e.g., 96 theorems) overlap with the theorems proved by its counterpart fine-tuned on the original datasets (e.g., 93 theorems), or are there distinct theorems unique to each?

### Soundness
3

### Presentation
2

### Contribution
2

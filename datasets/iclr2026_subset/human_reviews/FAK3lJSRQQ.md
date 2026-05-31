## Human Reviewer 1

### Summary
The authors propose ExLLM, a framework that enables the effective utilization of LLMs for molecular design without re-engineering or additional training. ExLLM employs a k-offspring and an evolving experience mechanism to achieve efficient exploration and maintain a non-redundant population. Moreover, the proposed feedback adapter allows the framework to perform consistent and stable optimization in multi-objective settings

### Strengths
- The paper presents a compelling framework that leverages pretrained LLMs as optimizer without requiring any additional training. Also, ExLLMs showed improved performance gains in both single-objective and multi-objective optimization tasks

- The k-offspring and evolving experience effectively enhance the exploration capability of pretrained LLMs while reducing the number of API calls and costs. This design choice represents a novel contribution that improves efficiency without sacrificing optimization quality

### Weaknesses
- In the paper, the comparison with other LLM-as-optimizer models is somewhat limited. While approaches such as OPRO, LMEA, and AlphaEvolve are mentioned, the paper does not provide experimental results against them in the molecular design. Moreover, other relevant molecular design-aware LLM frameworks (e.g., ChemCrow, LICO, MolReGPT, Prompt-MolOpt) are discussed but not empirically compared.

- The paper primarily relies on GPT-4o or Gemini, without evaluating open-source LLMs such as Llama[1] or Qwen[2].

- Although the work is positioned as an LLM optimizer for molecular design, the paper provides limited discussion on molecular design.

- Figure 1 could be improved for clarity. Some key components(e.g., k-offspring) are not visually highlighted, making it somewhat difficult for readers. 

[1] Dubey, Abhimanyu, et al. "The llama 3 herd of models." arXiv e-prints (2024): arXiv-2407.

[2] Yang, An, et al. "Qwen3 technical report." arXiv preprint arXiv:2505.09388 (2025).

### Questions
- (w1)The authors do not present experimental comparisons with other LLM-as-optimizer models in molecular design. While existing LLM optimizer studies (e.g., OPRO, LMEA, AlphaEvolve) may not be specifically designed for molecular design tasks, ExLLM also operates without explicit in-context learning, prompt engineering, or domain-specific feedback. Therefore, it seems feasible to evaluate these LLM optimizer frameworks on molecular design. In addition, could you clarify why MOLLEO was selected as the only molecular-design baseline(e.g., ChemCrow, LICO, MolReGPT, Prompt-MolOpt)? If there are practical constraints in evaluating agent-based frameworks or using external chemical tools, it would be helpful to mention that explicitly, and include comparisons with any executable models if possible.

-  (w2)The paper only presents results using GPT-4o and Gemini. However, it seems that other open-source LLMs such as Llama[1], Qwen[2] could also be applied to ExLLM. In particular, Qwen[2], which adopts a Mixture-of-Experts (MoE) architecture, is expected to offer advantages in terms of API calls and inference time. It would be helpful to include additional ablation experiments comparing their cost and performance.

-  (w3)Although the paper is positioned as an LLM optimizer for molecular design, there is little discussion related to the generated molecules. In particular, since k-offspring is introduced only in the ablation study, it would be helpful to include a brief analysis of the sampled offspring themselves.  Moreover, a pareto front plot and an oracle call curve (for PMO single-objective optimization) are not presented. 

- In Table 2(and Table 10), the reported diversity appears to be somewhat lower, even though uniqueness remains high. Could you elaborate on this observation? Is the lower diversity mainly due to differences in how the metric is defined, or should it be understood as a trade-off between fitness and diversity?

- Could you provide more details on the selection process? It could be viewed as a form of sampling, but it currently appears to be implemented solely as a weighted-sum operation. Are there any experiments comparing this approach with other selection methods? For example, methods such as Chebyshev scalarization sampling[3], Tchebycheff Scalarization[4], or Dirichlet distribution–based sampling[5] could also be considered. Are these approaches incorporated into the pareto front–based selector? Additional explanation of the fitness and pareto selectors would be helpful.

- In the appendix ‘7.9 NUMBER OF OUTPUT MOLECULES’, “Table??” appears to be a LaTeX mapping error. Please correct it.

[3] Chugh, Tinkle. "Scalarizing functions in Bayesian multiobjective optimization." 2020 IEEE Congress on Evolutionary Computation (CEC). IEEE, 2020.

[4] Lin, Xi, et al. "Smooth tchebycheff scalarization for multi-objective optimization." arXiv preprint arXiv:2402.19078 (2024).

[5] Shin, Dong-Hee, et al. "Offline Model-based Optimization for Real-World Molecular Discovery." Forty-second International Conference on Machine Learning.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This work introduces an LLM-as-optimizer framework with three contributions: an evolving experience snippet, a k-offspring scheme, and a feedback adapter for molecular design and optimization. Under fixed evaluation budgets this approach improves on PMO benchmark, across single- and multi-objective molecular optimization settings.

### Strengths
The manuscript reads mostly clearly.
Strong results on PMO benchmark.
The experiments included extra in addition to small molecules such as peptides.
Six-objective experiments with good results are novel.

### Weaknesses
The three main contributions seem to focus on “low cost” but discussion on cost perspective significantly lacks. 
The framework looks close to MOLLEO, as LLMs handle mutation and crossover on the parent molecules and the evaluation and update pools rely on conventional metrics, even if the templates looked carefully crafted in their overview.

Figure 1 and the method section do not provide a clear end-to-end overview. Subsections in Section 3 Method do not fully match the figure. The paper should clarify how the next population is selected in single vs multi objective cases, given that Pareto selection applies only to multi objective settings. 

Editorial issues. Please look through the whole manuscript and fix indexing. Below are some wrong referencing I have found.
-line 141 says Figure 8 for the framework overview, but I assume they refer to Figure 1.
-Table 2 is missing some boldface for some best results.
-Around lines 316-317, the text points to Table 10 which appears to mean Table 2.

More concerns and questions will be placed in Questions section below.

### Questions
This lies with Weakness 1 regarding the main contributions. Could you compare cost directly and show how the framework reduces cost, for example with ablations or matched cost vs quality analysis in detail?

Reading through the method and the overview figure, I assume the task-specific templates and the prompts seem very important, yet details are limited. Please describe design choices.

The LLM-as-optimizer idea is emphasized, but the final decision makers are a fitness-based selector and a Pareto front-based selector for next populations and choosing the best molecules. Have you done some ablations that replaces LLM proposals with molecules that are generated in rule-based way and optimizes with the fitness/pareto-based selectors?

In Figure 2 in Ablation study, GPT-based variants are consistently better in both single and five objective settings regardless of k. The curves over k do not show a stable pattern, especially in multi-objective setting. Clear evidence that k  offspring scheme itself actually add meaningful contribution to the framework should be included. 

In multi objective molecular optimization, some objectives like QED and SA are easier than others. In the five-objective setting, can you provide evidence that the framework balances the objectives rather than leaning on easy objectives? For example, through per-objective improvements and coverage of the Pareto front.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper presents ExLLM (Experience-Enhanced LLM Optimization), which is a framework that uses LLM as optimizers for molecular design and other large discrete optimization problems. The proposed framework addresses key limitations of existing LLM-based methods for molecular design, which are often heavily prompt-dependent, require additional training, and lack memory mechanisms suited for large-scale iterative search. ExLLM consists of three main components: (1) an evolving experience mechanism that maintains a single, compact memory snippet updated each generation to distill non-redundant insights from good and bad examples, avoiding the memory bloat and exploration collapse seen in retrieval-style memories; (2) a k-offspring sampling scheme that generates k candidate molecules per LLM call by exploiting autoregressive factorization, widening exploration while reducing the number of LLM queries needed; and (3) a feedback adapter that normalizes multiple objectives into comparable vectors for Pareto-based selection and formats constraints/expert feedback into structured text for the next iteration. The framework uses a hybrid selection strategy, choosing half the population by scalar fitness (weighted sum of normalized objectives) and half from the Pareto front. The experience is injected into prompts with probability p_exp to balance exploitation and exploration.

### Strengths
1. I appreciate that the authors address multi-objective optimization, which many molecular generation works either omit or treat superficially. I personally believe that multi-objective optimization is critically important for real-world molecular discovery.

2. The training-free approach requires no additional model training, thereby reducing computational costs compared to other existing methods that require retraining for each new task or property.

3. Generating multiple offspring per LLM call reduces the number of required queries and thus improves computational efficiency.

### Weaknesses
**1. Limited Technical Novelty**
- Using LLMs for molecular design is no longer novel and has become a well-established research direction. The prior works mentioned in the introduction (ChemCrow, LICO, MolReGPT, Prompt-MolOpt, MOLLEO) already demonstrate that LLMs can be effectively applied to molecular generation/optimization tasks.

- The core contribution appears to be incremental tweaking of existing components rather than methodological innovation. The evolving experience mechanism is adapted from prior work (ReEvo, ExpeL as acknowledged by authors), the k-offspring strategy is a straightforward application of autoregressive sampling of LLMs, and the feedback adapter is essentially normalization plus text formatting. Each component individually represents a relatively minor modification to existing techniques.

**2. Insufficient Baseline Comparisons for LLM-based Methods**
- The authors mention multiple LLM-based molecular design methods in the introduction (ChemCrow, LICO, MolReGPT, Prompt-MolOpt) but only include MOLLEO as a competing LLM-based baseline in the experiments. This creates an incomplete picture of how ExLLM compares to the broader landscape of LLM-based molecular optimization approaches.

**3. Poor Paper Organization and Presentation** 
- Section 2.3 contains only the text "We have put this part to appendix 7.2," which is highly unusual and unprofessional. While moving supplementary details to an appendix is acceptable practice, completely omitting a main-text section and relegating all content to the appendix is inappropriate formatting.

- This organizational choice disrupts the flow of the paper and suggests either careless preparation or an attempt to circumvent page limits. If the LLM-as-optimizer and memory mechanism background is important enough to warrant a section number, it deserves at least a brief summary in the main text with details deferred to the appendix.

**4. Insufficient ablation studies and analysis**
- No ablation on the hybrid selection strategy (50% fitness-based, 50% Pareto-based). Why this specific ratio? How sensitive is performance to this choice?

- I am still confused and not fully convinced about the clear beneficial effects of the hybrid selection strategy.

- The paper claims the experience mechanism is "lightweight" and "low-redundancy," but provides no quantitative analysis of memory consumption, prompt token counts over time, or computational overhead compared to the retrieval-style baseline beyond Table 1.

### Questions
1. The paper exclusively uses two proprietary LLMs (GPT-4o and Gemini) without justifying this choice or exploring alternatives. Why were only these specific models selected? Would the proposed framework work with open-source general-purpose LLMs such as Llama, Mistral, Qwen, or DeepSeek? 
2. Also, would chemistry-specific LLMs such as ChemLLM or Galactica potentially perform better given their domain-specific pretraining? 

3. The paper extensively evaluates three initialization schemes (worst-init, random-init, best-init) in Table 2, but provides no justification for why these specific schemes are relevant to real-world molecular discovery. In practical drug discovery scenarios, what situation would correspond to "worst-init" where researchers deliberately start with the 100 worst-performing molecules? The paper should clarify what real-world molecular discovery processes these initialization schemes are meant to simulate, and why demonstrating robustness across all three is important 

4. The paper acknowledges in Table 2 that "ExLLM delivers substantial gains over the initial populations in all three init schemes, while trading some diversity for finer exploitation" and that "the diversity of the final top-100 set is somewhat lower." However, molecular diversity is a crucial consideration in real-world drug discovery for several reasons: (1) diverse chemical scaffolds provide multiple starting points for lead optimization; (2) diversity helps hedge against failures in later stages (e.g., toxicity, synthesis issues); (3) intellectual property strategies often require exploring diverse chemical matter. ExLLM's diversity scores are substantially lower than several baselines. How do the authors justify sacrificing molecular diversity for higher fitness in the context of real-world applications where diversity is often explicitly required? Would the framework be unsuitable for scaffold-hopping or exploring novel chemical space?

5. The evolving experience mechanism maintains a single, continually updated snippet that is overwritten each generation. This unidirectional update raises concerns about catastrophic forgetting. For example, early in optimization, certain structural patterns might seem unimportant and get discarded, but they could become critical after the search moves to a different region of chemical space. The paper provides no mechanism to prevent or detect such forgetting.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper closely follows the overall workflow of MOLLEO for multi-objective molecular optimization. The main contribution lies in introducing several practical techniques for updating the memory pool and reducing the computational cost associated with feedback processing.

### Strengths
The related work section is well-organized and provides a clear overview of prior research. The paper introduces several strategies to reduce the computational cost in LLM-based molecular optimization, particularly within the MOLLEO framework.

### Weaknesses
Overall, the paper does not appear to provide a method with substantial novelty. The proposed approach largely follows the MOLLEO process, and the modifications in the memory update and feedback stages seem a little incremental rather than fundamentally new. The contribution is closer to presenting practical tips for reducing LLM API calling costs and prompt engineering strategies, rather than introducing a novel algorithmic framework.

Regarding the presentation of results, the main tables could be improved for clarity. The current main table contains many blank entries, which hurts readability. I recommend condensing the main table by focusing on a subset of objectives (e.g., 3–6 or 4–6 objectives) and reporting full results in the Appendix. Since the paper also includes experiments with 1–6 objectives, it would be more informative to include strong baselines such as MOLLEO, DyMol, and Genetic-GFN for the higher-dimensional objective settings in the main comparison.

Additionally, the result tables would benefit from further refinement. The “Worst” and “Best initial” columns contain many empty cells, and it is unclear whether they need to be part of the main results. These analyses feel closer to ablation-level studies and may be more suitable for the Appendix rather than presented as primary results.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4
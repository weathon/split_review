# TODO: Enhancing LLM Alignment with Ternary Preferences

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Aligning large language models (LLMs) with human intent is critical for enhancing their performance across a variety of tasks. Standard alignment techniques, such as Direct Preference Optimization (DPO), often rely on the binary Bradley-Terry (BT) model, which can struggle to capture the complexities of human preferences—particularly in the presence of noisy or inconsistent labels and frequent ties. To address these limitations, we introduce the \underline{\textbf{T}}ie-rank \underline{\textbf{O}}riented \underline{\textbf{B}}radley-\underline{\textbf{T}}erry model (TOBT), an extension of the BT model that explicitly incorporates ties, enabling more nuanced preference representation. Building on this, we propose \underline{\textbf{T}}ie-rank \underline{\textbf{O}}riented \underline{\textbf{D}}irect Preference \underline{\textbf{O}}ptimization (TODO), a novel alignment algorithm that leverages TOBT's ternary ranking system to improve preference alignment. In evaluations on Mistral-7B and Llama 3-8B models, TODO consistently outperforms DPO in modeling preferences across both in-distribution and out-of-distribution datasets. Additional assessments using MT Bench and benchmarks such as Piqa, ARC-c, and MMLU further demonstrate TODO's superior alignment performance. Notably, TODO also shows strong results in binary preference alignment, highlighting its versatility and potential for broader integration into LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors present an interesting approach to enhancing the alignment of LLMs through the use of ternary preferences. A limitation of binary models is their inability to effectively address tie situations in preference data, where two responses may be equally preferred or indistinguishable in quality. To address this issue, the authors propose an extension of the BT model, termed the Tie-rank Oriented Bradley-Terry (TOBT) model, which accommodates ties in preference relations. Building on this framework, they introduce a novel alignment algorithm called Tie-rank Oriented Direct Preference Optimization (TODO), specifically designed to manage ternary preference data that includes "prefer," "tie," and "disprefer." They conduct experiments comparing their TODO algorithm with the DPO. The results demonstrate that TODO consistently outperforms DPO in modeling preferences across both in-distribution and out-of-distribution datasets, as well as on several benchmarks. The paper also provides an analysis of the key factors contributing to TODO's improved performance.

### Strengths
1. The paper introduces a novel extension to the Bradley-Terry model by incorporating ties through the Tie-rank Oriented Bradley-Terry (TOBT) model. This allows for more nuanced preference modeling in LLM alignment.
  
2. The theoretical foundations of the TOBT model and the TODO algorithm are well-developed. The authors provide detailed derivations and clarify how the tie parameter α is integrated into the model.
  
3. The paper is generally well-written and structured. The methodology, including the mathematical formulations and the proposed algorithm, is clearly presented. The inclusion of figures and tables aids in understanding the results.

### Weaknesses
1. The extension from the traditional Bradley-Terry (BT) model to the Tie-rank Oriented BT (TOBT) model is central to the proposed method. However, the paper provides limited theoretical justification for this extension. The choice of the parameter α in the TOBT model appears somewhat arbitrary, and while Appendix A.3 attempts to justify its value based on balancing loss values, there is no rigorous analysis or sensitivity study demonstrating how different values of α affect the model's performance. Specifically, the paper lacks a detailed analysis of how the magnitude of α influences the gradient during training, and how this might lead to instability or divergence. Additionally, the paper lacks a thorough exploration of the probabilistic interpretation and properties of the TOBT model compared to the original BT model. A deeper theoretical analysis would strengthen the foundation of the proposed method and clarify its advantages and limitations.

2. The experiments primarily focus on datasets derived from Ultrafeedback and a select few benchmarks. While Ultrafeedback is a valuable resource, it may not fully represent the diversity and complexity of real-world human preference data, especially in terms of the prevalence and nature of tie data. The paper does not evaluate the method on more varied datasets, such as those involving different languages, domains, or more complex tasks where tie situations might behave differently. This raises concerns about the generalizability of the proposed method to broader applications and different types of data. For example, datasets with more subjective or nuanced tasks might exhibit different tie patterns, and it's unclear if the proposed method would perform consistently well across such scenarios.

3. The paper compares the proposed TODO method primarily against Direct Preference Optimization (DPO). However, there are other existing methods in preference alignment and RLHF that could serve as relevant baselines, such as PPO, RPO, IPO), and KTO. By not including these comparisons, it is difficult to assess how TODO stands relative to the other existing methods in preference alignment. Including a broader range of baselines would provide a more comprehensive evaluation and strengthen the empirical claims. The lack of comparison with methods that also use a form of preference optimization makes it difficult to ascertain the specific advantages of the proposed approach.

4. While the paper highlights the prevalence of tie data in preference datasets and proposes methods to utilize it, But ties may often result from annotator uncertainty, ambiguity in prompts or responses, or inconsistencies among annotators. By treating tie data as equally informative as clear preferences without accounting for potential annotation noise or bias, the method might be incorporating noisy signals into the model. A discussion on how to handle annotation noise, perhaps by incorporating methods to assess annotator reliability or confidence, would strengthen the approach. Additionally, exploring strategies to improve data quality or to model uncertainty explicitly could enhance the effectiveness of the proposed method. For example, the paper could explore methods to weight tie data based on annotator agreement or confidence scores.

### Questions
1. Can TODO be integrated with other alignment methods beyond DPO, such as reinforcement learning from human feedback (RLHF)? If so, how would it interface with existing reward models?
  
2. Are there any trade-offs in using the TOBT model compared to traditional binary preference models? For example, does incorporating tie data introduce additional computational complexity or affect convergence?

### Soundness
2

### Presentation
3

### Contribution
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
This work aims to directly model the fact that binary preference models such as the standard and well-known Bradley-Terry (BT) model cannot integrate ties and uncertainties when working with preference data. The main idea is thus the 'ternarization' of the original binary BT model that takes into account possible ties, where 'ties' are modeled via an additional parameter alpha. A large part of the paper is then dedicated to motivating and deriving the ternary (i.e., tie-aware) BT model, and then, based on that model on deriving and explaining TODO, a tie-aware extension of the original DPO algorithm for preference optimization. Experiments with two standard models (Mistral and LLaMA) and with a spectrum of standard datasets demonstrate the benefits of the TODO approach over its base binary DPO approach, even in setups without any ties. The authors then aim to provide some theoretical and empirically grounded interpretations on what makes TODO a more expressive and better-performing alternative to DPO.

### Strengths
- The paper is well written, and it is very easy to understand its core motivations and follow how the entire derivation of the tie-aware BT model and the corresponding TODO model unfolds from the main design assumptions.
- The provided results offer reasonable evidence on the benefits of TODO over DPO. The chosen evaluation data and models are adequate.
- The paper raises awareness on modeling ties in preference optimizations, where such valuable data often gets discarded under inadequate models or models with too strong assumptions (such as the binary BT) - taking into account finer granularity of preference data might yield further improvements in this line of work, and this paper sheds some new light on this link.

### Weaknesses
 - One of the core issues with the work lies in the fact that other researchers in 'less recent times' have already attempted and derived generalised versions of the BT model, which better align with multi-class (i.e., non-binary) problems. Even a cursory search online reveals some very relevant literature which is not cited nor discussed in this work. I would require the authors to provide a thorough overview of that relevant work and discuss why a new (tie-aware) derivation might be needed here, and whether previous solutions could be repurposed for the extension of the original, binary BT model. For instance, I refer to the following relevant work here:
-- https://dl.acm.org/doi/pdf/10.5555/1248547.1248551
-- https://proceedings.neurips.cc/paper_files/paper/2004/hash/825f9cd5f0390bc77c1fed3c94885c87-Abstract.html
-- https://link.springer.com/article/10.1007/s10994-011-5240-0
See also Q1 related to this comment.

- Another concern is the lack of generality of TODO as it is derived directly as an extension of one concrete model: DPO. Following that, only DPO is also used as the only relevant baseline, and I see at least two potential issues here:
(i) While the authors state at the very end of the paper that the approach is "(...) not only limited to direct preference optimization but is also compatible with various online and offline preference optimization policies and can be employed for reward model training...", already this work should have coupled the idea with another preference optimization method to show this decoupling. In essence, the authors should both theoretically and empirically discern between making 'ternary decisions' and deriving enhanced preference optimization algorithms that incorporate the possibility to do ternary decisions. 
(ii) DPO is used as the only baseline, while there is a plethora of other online and offline preference optimization algorithms out there, where some of them should have been included as baselines and reference points. For instance, the KTO approach disposes of the need to even collect preference data and model preference decisions as part of the process (unlike DPO or PPO). One core question is then: can we simply use KTO instead of 'ternarizing DPO'? What would be the benefits of TODO versus KTO? 
(iii) The authors very vaguely comment in lines 122-123 that previous preference alignment studies "...overlook the potential of leveraging tied preference data to refine alignment, whereas our approach is complementary to most of them." It is unclear to which studies the proposed approach is complementary, and as mentioned above - it does not offer sufficient empirical validations to demonstrate that the approach is better than KTO, IPO, etc. I would suggest including direct comparisons to these other methods beyond DPO.

- All the experiments are based on the UltraFeedback dataset, and the training set size is limited to 20k data instances. The training set size might be a very important factor in defining the final performance (and benefits of ternary vs binary vs unary modeling as with KTO). Therefore, the paper should investigate how the standard DPO and KTO behave in comparison to TODO also for larger datasets (e.g., using the full UltraFeedback). Ideally, the work should experiment with another preference alignment dataset as well beyond UF, I would strongly suggest running experiments with another dataset, and compare against methods such as DPO and KTO also on larger datasets.

I am willing to reconsider my initial assessment and position if these central weaknesses get addressed by the authors.

### Questions
Q1 (related to the first, main point listed under "Weaknesses"). Speaking of previous work, how does your tie-aware BT model differ from or improve upon existing multi-class generalizations of the BT model that I provided under weaknesses plus the ones that you also cited? Are there any components, ideas or other aspects of prior approaches to BT generalisation that could be incorporated into or compared against your method?

Q2. It seems that the results are also dependent on the tie data ratio in the full training set of 20k instances. How can a practitioner determine the best (or task-optimal) choice of the tie data ratio? What if tie data is lacking for some specific use-cases?

Q3. How were hyperparameters from Appendix A.9 selected? Is there any substantial variation of the results based on the hyper-parameters?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the inclusion of ties in the DPO framework to be able to model preferences in a more nuanced way. It derives a ternary model for preferences analogously to the binary Bradley-Terry model, and defines a novel preference learning objective (TODO) accordingly. Experiments are conducted by preference-tuning Llama3 and Mistral with preferences from Ultrafeedback with varying proportions of ties, and evaluating them in and out of domain, and on downstream tasks. The new TODO objective outperforms DPO in preference modeling and downstream tasks across the bench.

### Strengths
1. The idea is well motivated, as ties are relevant especially in human preference elicitation and can be expected to become even more prevalent the stronger generative models get. 
2. The experiments are strongly supporting the new objective, the results are convincing.
3. The proposed solution is based on a solid intuition and supported by detailed derivation.

### Weaknesses
The only claim that is empirically not supported is that TODO “exhibits better robustness against potential noise in binary preference data.” There is no experiment studying noise in preferences (ties do not need to be caused by noise, they also present adequate equalness). One could easily set up an experiment with artificial noise added to preferences to test this hypothesis.

### Questions
1. What is the intuition for why it works better than DPO even without ties in the data?
2. What is the naturally occurring frequency of ties in the UltraFeedback data?
3. How does it compare empirically against related approaches, especially ODPO?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Existing LLM alignment algorithms rely on the binary BradleyTerry model, which is hard to capture ties in preference. To address this issue, this paper proposes Tie-rank Oriented Direct Preference Optimization (TODO), an alignment algorithm that  leverages TOBT’s ternary ranking system. 

TODO rewrites the ranking probability in BradleyTerry to add tie instances and derive the loss function of TODO. Experimental results verify the effectiveness of TODO.

### Strengths
The strengths of this paper can be listed as follows:
1. The motivation of this paper is clear and reasonable. Starting with the improvement of the BT model, this paper introduces the tie instance. This research idea is consistent with theoretical improvements of BT model.
2. The paper writing is good. I think it is easy to follow the authors' research ideas.
3. Experimental settings are detailed and well organized.

### Weaknesses
The weaknesses of this paper can be listed as follows:
1. **Limited baselines.** This paper only provides the comparison of experimental results between TODO and DPO, which is relatively limited. It is necessary to include a wider range of baselines, particularly those that address similar preference optimization objectives. For example, methods like SimPO, which also aims to improve preference optimization, should be included to provide a more comprehensive comparison.
2. **Limited improvements.** The improvement of TODO over DPO is limited as shown in table 2 and table 3. The performance gains on reasoning tasks are marginal, raising questions about the practical significance of the proposed method in these areas. The lack of substantial improvement in these tasks suggests that the benefits of incorporating tie preferences may not be universally applicable across all types of LLM tasks.

### Questions
I am also very curious that if the performance of LLM alignment will improve if you just simply filter out the tie preference pairs out of the training set.

### Soundness
3

### Presentation
3

### Contribution
3

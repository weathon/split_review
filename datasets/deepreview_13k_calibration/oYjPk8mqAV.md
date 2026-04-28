# Magnushammer: A Transformer-Based Approach to Premise Selection

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
This paper presents a novel approach to premise selection, a crucial reasoning task in automated theorem proving. Traditionally, symbolic methods that rely on extensive domain knowledge and engineering effort are applied to this task. In contrast, this work demonstrates that contrastive training with the transformer architecture can achieve higher-quality retrieval of relevant premises, without the engineering overhead. Our method, \method, outperforms the most advanced and widely used automation tool in interactive theorem proving called Sledgehammer. On the PISA and \minif2f benchmarks \method achieves $59.5\%$ (against $38.3\%$) and $34.0\%$ (against $20.9\%$) success rates, respectively. By combining \method with a language-model-based automated theorem prover, we further improve the state-of-the-art proof success rate from $57.0\%$ to $71.0\%$ on the PISA benchmark using $4$x fewer parameters. Moreover, we develop and open source a novel dataset for premise selection,
   containing textual representations of (\textit{proof state}, \textit{relevant premise}) pairs. To the best of our knowledge, this is the largest available premise selection dataset, and the first one for the Isabelle proof assistant.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a language-model-based premise selection tool, Magnushammer, for the Proof assistant Isabelle. Given the current textual proof state, Magnushammer, is able to select a set of relevant premises based on trained transformer models. This selection is two-staged: (1) SELECT: an efficient step that selects premises with the highest representation similarity to the given proof state; (2) RERANK: re-rank the selected premises based on a score outputted by a binary classifier predicting whether the proof state and the premise are relevant. The models in both stages are trained contrastively, upon the data collected from human-proof libraries and alternative proofs from Sledgehammer. During experiments, Magnushammer shows significant improvement over Sledgehammer. The authors also open-sourced the collected premise-selection dataset.

### Strengths
The paper proposes a novel approach to premise selection, which was previously considered a difficult task for LLMs since the length of relevant premises is usually much larger than what LLMs can handle. With batch-contrastive learning and careful data design and collection, Magnushammer retrieves premises instead of generating them using Transformers, showing impressive performance on theorem-proving benchmarks.

•	The experiment design is generally sound and compelling. The experiment separates the training and test data and evaluates the quality of premise selection in both single-step (direct evaluation) and multi-step (integration with Thor) tasks. The authors also present the impact of the number of selected premises on the proof rate, as an alternative measurement of the premise selection quality.

•	The ablation study is comprehensive, covering the pre-trained model, model size, dataset size, and compute budget.

### Weaknesses
The presentation of why the premise selection was considered difficult for LLMs, and how the proposed method tackles these difficulties is somehow weak. Some more examples and explanations/discussion on LLM/contrastive learning would help.

•	Section 6 mentions GPT-f, PACT, Thor, and other LLM-based theorem-proving efforts, highlighting their diverse focuses. It would be nice if the authors provided a more insightful and coherent discussion on how different aspects are connected (e.g., premise selection, tactic prediction, proof step search), how the previous works explicitly or implicitly tackled the premise selection problem, and how the proposed method is advancing the area.

•	Section 3 Training part mentions that “This gives N-1+M negatives per proof state in one batch”. Is it possible that a positive premise for one state is also positive for another state in the same batch? Did you select positive examples intentionally avoiding this possibility, or, in this case, the negative examples are less than N-1+M?

•	During the evaluation, for each proof state, Magnushammer parallelly checks whether a proof can be completed from premise subsets of different sizes. The author claims that similar techniques are also implemented in Sledgehammer. The author can explain more on this point to ensure the experimental comparison between Magnushammer and Sledgehammer is fair, e.g., in terms of parallelism, number of selected subsets, and their sizes.

•	Minor formatting issue: the reference of Thor in Section D.2 on Pg21.

### Questions
•	The author mentioned that the MAPL dataset “decreases the probability of sampling false negatives while training contrastively”. Could the author provide further details on the likelihood of a premise being positive if it is not found by human-proof collections and Sledgehammer? Additionally, are there other methods to validate or enhance the confidence that it is a true negative? Also, the influence of false negatives on batch-contrastive learning can be elaborated.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the field of automated theorem proving, premise selection is the process of selecting a subset of mathematical statements that are already known to be true as a set of premises to build new knowledge. In this work, the authors introduce MAGNUSHAMMER, a premise selection technique based on transformers.

### Strengths
The idea of using transformers in for premise selection is quite interesting. In my opinion, the main strength of this paper the fact that this approach was able to outperform an automated theorem prover based on similar paradigm by a good margin. More specifically, the new approach obtained a proof rate of 59.5%, while sledgehammer, which is one of the most well known premise selection tools for Isabelle, obtained a proof rate of 38.3%. 

The authors also contribute with a large dataset for benchmark of premise selection paradigms. 

Finally, the authors provide a careful analysis of their approach by analysing the dependence on quantities such as model size, dataset size. According to their results, when resources are moderate, their approach outperforms existing techniques.

### Weaknesses
The main drawback seems to be the fact that the tools were evaluated only on two datasets (PISA and miniF2F). This limits the generalizability of the findings. Specifically, both datasets are derived from the Isabelle theorem prover, which might introduce a bias towards this specific environment. The performance of MAGNUSHAMMER on datasets from other theorem provers, which may have different logical structures and proof styles, is unknown. Furthermore, the datasets might not fully cover the diversity of mathematical theorems and proof techniques, potentially leading to an overestimation of the approach's effectiveness in broader contexts. The lack of evaluation on datasets with different characteristics makes it difficult to assess the robustness of the proposed method.

### Questions
What are other suitable datasets for the evaluation of tools for premise selection?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper Magnushammer, a transformer model trained for premise selection on Isabelle. They first build a training set of premise selection from human-written proofs and machine-generated proofs produced by Sledgehammer. Magnushammer select relevant premises in two steps, first select a larger set of premises from all candidate based on cosine similarity of embeddings from a transformer model, then rerank these the selected premises by concating them with the proof state and feeding the new sequences into the transformer for binary classification. Experiments validate that, compared to Sledgehammer, better premise selection using Magnushammer leads to significant improvement for theorem proving with Thor on the PISA (57% -> 71%) and miniF2F (29.9% -> 37.3%) dataset.

### Strengths
1 Similar to LeanDojo, this paper demonstrates that better premise selection is crucial for the success of theorem proving. 
2 The proposed approach is technically sound, with properly designed select and rerank steps, InfoNEC and BCE losses and data collection steps.
3 Experiments demonstrate significant improvement resulting from Magnushammer. 
4 The proposed dataset for premise selection could facilitate the future progress for automated theorem proving.

### Weaknesses
Still, the main story of this paper is almost the same as LeanDojo. The proposed two-step pipeline and training method are also commonly used.

### Questions
1 It is great to know we could advance theorem proving by developing better premise selection approaches. My question is what the upper bound is given our current recipe. Is it possible to obtain the results of Thor with ground truth premise selection?
2 Did you retrain Thor with Magnushammer or just apply the original Thor trained with Sledgehammer to Magnushammer?
3 Could you quantitatively evaluate the contribution of Magnushammer for theorem proving with Thor, such as how many proof steps call Magnushammer in your test.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method for premise selection in automated theorem proving. The proposed method is based on training a transformer model on the text of the lemmas that are available in a library. The proposed method improves the testing accuracy of AI assistants on some benchmarks.

### Strengths
The open source premise selection dataset appears to me as a useful contribution for the community.

I found the approach and the proposed method interesting. 

Paper is well structured and its writing is clear.

### Weaknesses
The main shortcoming that appears to me is the lack of comparison with recent methods such as LeanDojo. Perhaps authors can address this during the rebuttal, clarifying the advantage of their proposed method.

Specifically, in the list of novel contributions of the paper, the first item is stated to be the use of contrastive learning for premise selection. However, contrastive learning was previously used in LeanDojo. It would be helpful if authors clarify the specifics of their contribution compared to previous methods.

-----

Moreover, authors have not cited the reference below which also trains a GPT model on mathematical statements. It seems that the authors' use of the GPT-2 model has some similarities with the approach taken by the paper below. So, it is not clear to me whether authors' approach is as novel as it is claimed to be. I ask that authors clarify their contributions in relation to this reference as well.

[1] Polu, S., Han, J.M., Zheng, K., Baksys, M., Babuschkin, I. and Sutskever, I., 2022, September. Formal Mathematics Statement Curriculum Learning. In The Eleventh International Conference on Learning Representations.


------------
As a limitation of Sledgehammer, this paper mentions the need for handcrafted design. In contrast to Sledgehammer, it is mentioned that Magnushammer does not need handcrafted design and feature engineering. However, the choice of negative premises appeared to me as a handcrafted approach in Magnushammer. I do not think this is necessarily a shortcoming of the Magnushammer, but I think the benefits and contributions of the Magnushammer might have been magnified a bit.

### Questions
Would it be possible for the authors to expand on their improvement on the miniF2F benchmark? Specifically, I would be interested to know what are the specific unsolved theorems that Magnushammer was able to solve, and how complex are those proofs. When one tries to solve those theorems with Sledgehammer or other assistants, what exactly goes wrong, and what is the gap that Magnushammer can bridge while sledgehammer cannot? Are the premises that Magnushammer can find, and Sledgehammer fails to find, related to the premises that were chosen by the authors for their contrastive learning? I think giving maybe two or three examples (theorems from miniF2F that were solved by Magnushammer) would improve the presentation of this paper’s contribution.

Authors mention that one benefit of Magnushammer is that it can be trained on various languages, and it is not limited to Isabelle, etc. Have authors experimented with lean? I did not see any results on lean, but I might have missed it.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

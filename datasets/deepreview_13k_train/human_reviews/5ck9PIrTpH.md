# MathGAP: Out-of-Distribution Evaluation on Problems with Arbitrarily Complex Proofs

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Large language models (LLMs) can solve arithmetic word problems with high accuracy, but little is known about how well they generalize to problems that are more complex than the ones on which they have been trained. Empirical investigations of such questions are impeded by two major flaws of current evaluations: (i) much of the evaluation data is contaminated, in the sense that it has already been seen during training, and (ii) benchmark datasets do not capture how problem proofs may be arbitrarily complex in various ways. As a step towards addressing these issues, we present a framework for evaluating LLMs on problems with arbitrarily complex arithmetic proofs, called \evalname. \evalname generates problems that follow fixed proof specifications---along with chain-of-thought reasoning annotations---enabling systematic studies on generalization with respect to arithmetic proof complexity. We apply \evalname to analyze how in-context learning interacts with generalization to problems that have more complex proofs. We find that among the models tested, most show a significant decrease in performance as proofs get deeper and wider. This effect is more pronounced in complex, nonlinear proof structures, which are challenging even for GPT-4o. Surprisingly, providing in-context examples from the same distribution as the test set is not always beneficial for performance. In particular, zero-shot prompting as well as demonstrating a diverse range of examples that are less complex than the test data sometimes yield similar or higher accuracies.\looseness=-1

\vspace{-5pt}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MathGAP, a framework designed to evaluate large language models (LLMs) on mathematical word problems requiring proofs of arbitrary complexity. The authors address two critical issues in current evaluations: data contamination due to overlapping training and test sets, and benchmarks not reflecting the arbitrary complexity of problem proofs.

MathGAP uses proof trees characterized by properties such as depth, width, linearity, and ordering, enabling the generation of synthetic problems with controlled complexity and corresponding chain-of-thought (CoT) reasoning annotations. By systematically varying these properties, the framework assesses how well various LLMs generalize to problems more complex than those encountered during training or provided in-context.

The authors conduct comprehensive experiments that reveal model performance significantly declines as proof complexity increases, particularly for nonlinear proofs. Interestingly, providing in-context examples from the same distribution as the test set does not always enhance performance. The study sheds light on the limitations of current LLMs in handling complex reasoning tasks and offers insights into their generalization capabilities.

### Strengths
Addresses a Critical Gap: Tackles the underexplored area of evaluating LLMs on problems with arbitrary proof complexity. Directly addresses issues of data contamination and limited complexity in existing benchmarks.

Formalism and Clarity: Utilizes proof trees and logical forms to precisely characterize problem complexity. Well-structured and clearly written, with helpful figures enhancing understanding.

Comprehensive Experiments: Conducts extensive experiments across multiple dimensions of proof complexity (depth, width, linearity, ordering). Evaluates various state-of-the-art LLMs, providing valuable insights into model behaviors and limitations.

Insights into LLM Limitations and In-Context Learning: Reveals that model performance degrades with increasing complexity. Provides meaningful insights into the impact of different in-context learning strategies. Highlights the models' sensitivity to problem structure and ordering.

### Weaknesses
Synthetic Data Limitations and Linguistic Diversity: Synthetic problems may not capture the full linguistic and conceptual diversity of real-world problems. Reliance on templates could lead to repetitive linguistic patterns. The use of a limited set of templates for generating mathematical word problems could result in models learning to exploit superficial patterns in the text rather than developing a genuine understanding of the underlying mathematical concepts. This could lead to an overestimation of the models' true capabilities in handling more varied and complex real-world problems. The lack of diverse linguistic structures and phrasing might limit the generalizability of the findings.

Assumption of Reasoning Alignment: Assumes LLMs reason in ways closely aligned with the proposed proof trees. Models might use heuristics or patterns not captured by the formalism, affecting evaluation accuracy. The evaluation framework assumes that the models' reasoning process will mirror the structure of the predefined proof trees. However, LLMs might employ different strategies, such as shortcut reasoning or pattern matching, that do not align with these trees. This discrepancy could lead to an inaccurate assessment of the models' reasoning abilities, as the evaluation might not capture the actual processes used by the models.

Limited Error Analysis: Lacks a deep analysis of error types made by the models. More detailed error categorization could provide insights into reasoning limitations (e.g., arithmetic vs. logical errors). The current analysis provides limited insight into the specific types of errors made by the models. A more detailed error analysis, categorizing errors into arithmetic mistakes, logical fallacies, or other types of reasoning errors, would be beneficial. This would help in identifying specific weaknesses in the models' reasoning capabilities and guide future improvements.

### Questions
Have you considered incorporating paraphrasing techniques or using LLMs to generate more diverse linguistic expressions to increase variety and challenge the models? Incorporating more arithmetic relations, irrelevant information, larger numbers, or units to enrich tasks could help increase the diversity as well. 

How do you ensure that the proof tree structures accurately reflect LLMs' reasoning processes? Is there a risk that models might not utilize the intended inference paths?

Can you provide more detailed analyses to determine whether performance drops are due to arithmetic computation errors, logical reasoning mistakes, or other factors?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces MathGAP, a framework for evaluating LLMs' mathematical abilities. The paper notes two main motivations for creating MathGAP: 1) data leakage/contamination and 2) lack of comprehensive and systematic evaluation signals (e.g., OOD generalization, different complexity levels, etc.). The authors show that the performance of almost all LLMs drops as the difficulty (measured by depth/width of proof tree) increases. Moreover, the paper shows that LLMs are sensitive to the order in which input assumptions/axioms are presented, suggesting limitations in the perceived reasoning capabilities of LLMs.

### Strengths
1- Given the unfortunate hype over LLMs, I believe it is crucial to have objective and solid evaluation metrics for LLMs and separate science from hype. This is exactly what this work is aiming to do.  
2- The paper is extremely well written and the authors present the results very well.  
3- Overall, the experiments are well-designed. However, they could have been extended to provide more insights (see below).

### Weaknesses
1- It is not clear how much "new insight" this work provides as many of the results have already been reported in other similar contexts. For instance, Dziri et al. also has a similar notion of graph depth/width, and shows that by increasing depth and width for both ID/OOD setups the performance drops significantly (see Fig. 5 of [1] for example). However, some open questions have not been addressed yet. For instance, from the results, it is not clear why the Llama3-70B model has a near-perfect score on "linear depth" scenarios: is it because of its training data, scale, or something else? Moreover, why is the performance gap between linear/non-linear benchmarks so significant? Do we know why the LLMs struggle so much in the nonlinear problems (e.g., Figure 3 of the paper) even when depth is small?

2- I believe given the nature of MathGAP, the paper could have explored more fine-grained evaluation scenarios beyond the final accuracy with in-context prompts. For instance, according to the note in section 5, the number of shots is fixed to 12 and the footnote mentions that this is large enough according to another work. However, the impact of context on model performance on MathGAP is unclear: Does the number of shots have a similar impact on linear/non-linear setups? Why?

3- The paper does not mention how large the overall set of proper names and values were. For instance, we know that LLMs have token bias and this can have an impact on results [2]. In addition, it is not clear what range of numbers was used and how many of the mistakes were arithmetic mistakes versus logical mistakes.

4- The logical forms and inference rules used are relatively simple and may not capture more complex mathematical relationships. However, this is not a critical issue compared to other issues as we know that models still struggle in these simple cases as well.

Overall, I think the work is borderline in its current form. I believe this work has potential to have a significant contribution if it can provide more insights and explanations that lead to better understanding of LLMs.

### Questions
See the questions from my comments above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Paper presents a framework for systematically studying the OOD reasoning capabilities of LLMs by programmatically generating training and test examples. Paper also presents analysis of how existing models behave for MathGAP problems under different settings.

### Strengths
Originality
- Current LLM reasoning benchmarks are mostly comprised of fixed datasets, which might be susceptible to data leakage and do not offer a way change different characteristics of the datasets such as difficulty
- MathGAP offers a way to systematically change the different aspects of the problem, size as depth, width and (non)linearity of problem tree, and constructs new problems every time, allowing for more controlled experiments on OOD generalization

Quality/Clarity
- Paper is well written and easy to understand

Significance
- in addition to providing a new benchmark to study generalization, paper also conducts analysis of current LLMs behavior using the proposed benchmark
- Presents interesting findings such as some models performing better when given OOD in-context examples rather than IID in-context examples

### Weaknesses
MathGAP examples seem to mostly involve a certain type of arithmetic problem, it would be interesting to expand to scope to include other types of reasoning problems

It would also be interesting to also study the finetuning generalization behavior of LLMs

### Questions
See weaknesses

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
3

### Summary
This paper proposes a math proof benchmark, called MATHGap, by constructing proof trees with predefined predicates and inference rules. Evaluation on a number of LLMs shows that LLM's performance decreases as the proof complexity increases. Many LLMs do not do well in these problems.

### Strengths
1. The authors did a good job elaborating the method. Section 3 provides a good background for readers to understand the method.
2. Constructing out-of-domain math problems using the logical form is a good way to evaluate the math capabilities of LLMs.

### Weaknesses
1. Despite the many LLMs being tested, the paper seems to miss the latest state-of-the-art LLMs, including Llama 3.1, Llama 3.2 (since Llama 3.2 is only recently released, I understand that the authors did not have time to include it), and GPT-O1. This is rather important, because the linear problems were pretty well-resolved by GPT-4O, and Llama 3 is also already very competitive. Including the more recent models might change the conclusions. Therefore, the current conclusion seems a bit outdated.

2. The authors seem to relate the failure of LLM's performance on the more complicated proofs to the OOD generalization failures. However, this is not necessarily the case because it may as well just be the performance degradation due to the problems being more challenging. In many cases, the in-distribution examples do not improve the performance over OOD examples, which is evidence that the performance drop is due to increased difficulty, not the generalization gap.

3. The analysis in the paper looks a bit shallow. It does not show much insight into why and how the LLMs fail. For example, is the performance degradation as complexity increases simply due to the more proof steps? Namely, it may as well be the case that the error rate of each step is constant; it is just the increased number of steps that drive down the overall success rate. In this case, the model scales fine and it is just the success criterion that becomes more stringent. Also, what are the typical failure modes? Are the errors simple arithmetic errors, reasoning errors, or errors in parsing the final results? Why does the in-context example fail to improve the performance? Why is there a nonlinear relationship between the distance of the ordering and the performance? It would make the paper stronger if the authors could perform more experiments to answer these research questions.

4. The MATHGap dataset looks too constrained for me. It only contains 5 predicates and 5 inference rules. As a result, the linear problems seem too easy for the latest state-of-the-art models. It would be nice to study how the performance scales with the number of predicates and inference rules, and whether the LLMs can retrieve the correct inference rules where there are many.

### Questions
I would appreciate if the authors could investigate the research questions raised in the 'weaknesses' section. In addition -

Why were different predicates used in different parts of the analysis, i.e. comp and transfer for depth analysis, part-whole for width analysis, etc.?

### Soundness
3

### Presentation
4

### Contribution
2

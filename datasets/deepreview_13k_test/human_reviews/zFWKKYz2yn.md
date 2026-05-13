# Stability Analysis of Various Symbolic Rule Extraction Methods from Recurrent Neural Network

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
This paper analyzes two competing rule extraction methodologies: quantization and equivalence query. We trained $3600$ RNN models, extracting $18000$ DFA (Deterministic Finite Automata) with a quantization approach (k-means and SOM) and $3600$ DFA by equivalence query($L^{*}$) methods across $10$ initialization seeds. We sampled the datasets from  $7$ Tomita and $4$ Dyck grammars and trained them on $4$ RNN cells: LSTM, GRU, O2RNN, and MIRNN. The observations from our experiments establish the superior performance of O2RNN and quantization-based rule extraction over others. $L^{*}$, primarily proposed for regular grammars, performs similarly to quantization methods for Tomita languages when neural networks are perfectly trained. However, for partially trained RNNs, $L^{*}$ shows instability in the number of states in DFA, e.g., for Tomita 5 and Tomita 6 languages, $L^{*}$ produced more than $100$ states. In contrast, quantization methods result in rules with a number of states very close to ground truth DFA. Among RNN cells, O2RNN produces stable DFA consistently compared to other cells. For Dyck Languages, we observe that although GRU outperforms other RNNs in network performance, the DFA extracted by O2RNN has higher performance and better stability. The stability is computed as the standard deviation of accuracy on test sets on networks trained across $10$ seeds. On Dyck Languages, quantization methods outperformed $L^{*}$ with better stability in accuracy and the number of states. $L^{*}$ often showed instability in accuracy in the order of  $16\% - 22\%$ for GRU and MIRNN while deviation for quantization methods varied in $5\% - 15\%$. In many instances with LSTM and GRU,  DFA's extracted by $L^{*}$ even failed to beat chance accuracy ($50\%$), while those extracted by quantization method had standard deviation in the $7\%-17\%$ range. For O2RNN, both rule extraction methods had a deviation in the $0.5\% - 3\%$ range.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is an empirical study on the capability and stability of rule extraction of deterministic finite automata (DFA) of multiple regular languages by a number of RNNs. Results show that second-order RNNs like O2RNN have better stability in extracting DFAs than first-order ones like GRUs and LSTMs, validating prior theoretical work. The results also show that quantization-based approaches extract fewer states than equivalence query methods. In addition, this paper also contains many comparison analyses for the effects of different architecture hyperparams on rule extractions.

### Strengths
This paper establishes its conclusion through solid empirical investigations. By varying rule-extraction methods, languages, architectures, and a bunch of hyper-parameters, this paper gives some valuable information on RNNs' performance in these types of tasks, and how consistent they are. These results could in turn give some valuable feedback to the theoretical community, where the motivation of these questions is from.

A possible potential for the approach investigated in this work is that it could serve as inspiration for the design of tasks to understand the capability of other types of neural networks that could potentially receive context-free language as inputs (say when context-free language is used to evaluate language models' ability).

### Weaknesses
1. The way this paper motivates the reader, and how the background is introduced, is somewhat too narrowly focused such that only researchers working in the most vicinity of the DFA extraction area could appreciate it. 
2. Even though this paper aims to provide empirical validation of some prior theoretical results, its exposition of the theoretical background is a little incomplete and not well organized (for example, what is  $\mathcal{E}_f$ and what's its relation with $\mathcal{E}$ and $\mathcal{E}^*(f)$? What does the subscript $|_i$ means in notation $\mathcal{E}^*(f)|_i$?) I think the paper would benefit hugely from a rewriting of these sections, to fill the gap between rough discussions of prior works and actual mathematical backgrounds and the question this paper is tackling.
3. The importance of the key evaluation metrics is not well motivated, and corresponding results are not well explained. For example, this paper should motivate more on why the number of extracted states can be used to evaluate DFA extraction strategies, and why lower numbers are preferred (yes the conclusion section contains better forms of your research questions but still why aren't they presented earlier?). 
4. The overall significance of the results in this paper is limited by the paper's choice to study only RNNs and rule extraction approaches, as they do not imply any further empirical messages, as the paper has not pointed to any other potential implications.

### Questions
See above weaknesses.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper conducts an empirical analysis of two competing methodologies for rule extraction—quantization and equivalence query—with the goal of elucidating the internal mechanisms of diverse RNN architectures. The authors identify specific scenarios where each strategy proves effective, and they substantiate their findings through comprehensive experiments designed to validate the presented conclusions.

### Strengths
The paper is well presented, by providing substantial background information and experiments.

### Weaknesses
See questions.

### Questions
Honestly, my familiarity with current RNN research, including rule extraction strategies, is limited. Consequently, I find it inappropriate to assess the topic, method, or the novelty of the work. However, I do have several questions for discussion.

- It would enhance the paper if the authors could furnish additional insights or intuition regarding the significance of exploring the stability of rule extraction strategies. Alternatively, a clearer definition of stability in this context would also be helpful. In the current work, stability appears to be synonymous with the variance of performance.

- A more thorough justification for the conclusion would be beneficial. Instead of solely benchmarking several methods across various settings, delving into the rationale behind the conclusions drawn would strengthen the paper and provide a more comprehensive perspective.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the efficiency and stability of various RNN architectures in the task of DFA extraction. It also compares the stability of two rule extraction methods, quantization and equivalence query, applied to trained RNNs. The findings indicate that the quantization-based approach is both more stable and generally outperforms the equivalence query method. Additionally, the study reveals that the DFA extracted using O2RNN surpasses other RNN architectures in terms of performance and stability.

### Strengths
To the best of my knowledge, this is the first paper that delves into the stability of rule extraction methods from trained RNNs. The paper is well-structured and straightforward. Moreover, the experiments conducted are thorough and systematic, and the results are indeed potentially useful in practice. I believe this work will be a solid contribution to the community.

### Weaknesses
I think the mathematical formulation of the problems considered in this paper can be more precise and more detailed, to make it easier to understand.

### Questions
No.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

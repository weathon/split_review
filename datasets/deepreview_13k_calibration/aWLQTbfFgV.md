# Training Neural Networks as Recognizers of Formal Languages

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Characterizing the computational power of neural network architectures in terms of formal language theory remains a crucial line of research, as it describes lower and upper bounds on the reasoning capabilities of modern AI. However, when empirically testing these bounds, existing work often leaves a discrepancy between experiments and the formal claims they are meant to support. The problem is that formal language theory pertains specifically to recognizers: machines that receive a string as input and classify whether it belongs to a language. On the other hand, it is common to instead use proxy tasks that are similar in only an informal sense, such as language modeling or sequence-to-sequence transduction. We correct this mismatch by training and evaluating neural networks directly as binary classifiers of strings, using a general method that can be applied to a wide variety of languages. As part of this, we extend an algorithm recently proposed by \ifanonymoussubmissionmode{}\citet{anonymous-2024-causal}\else{}\citet{snaebjarnarson-etal-2024-causal}\fi{} to do length-controlled sampling of strings from regular languages, with much better asymptotic time complexity than previous methods. We provide results on a variety of languages across the Chomsky hierarchy for three neural architectures: a simple RNN, an LSTM, and a causally-masked transformer. We find that the RNN and LSTM often outperform the transformer, and that auxiliary training objectives such as language modeling can help, although no single objective uniformly improves performance across languages and architectures. Our contributions will facilitate theoretically sound empirical testing of language recognition claims in future work. We have released our datasets as a benchmark called FLaRe\footnote{\ifanonymoussubmissionmode{}Included in the supplementary material.\footnote{\ifanonymoussubmissionmode{}Included in the supplementary material

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores formal language recognition tasks with different architectures. The authors argue that the primary motivation underlying formal language theory is language recognition and not next token prediction as used by existing literature. As such, they propose a novel data generation algorithm that can generate positive and hard negative examples from a diverse set of formal languages. Finally, through extensive experiments, they show that RNNs and LSTMs generally outperform transformer architectures.

### Strengths
The strength of the paper lies in its motivation to quantify gaps between different architectures by formal language recognition tasks. The authors start with a discussion on the basis of formal language theory, and how existing works differ from this basis in their experimental settings. Then, they propose a novel data generation algorithm that can sample positive and hard negative samples from each formal language. The algorithm has been discussed in great detail, and the running time has been contrasted with naive data generation algorithms.

The authors then conduct extensive comparisons of RNNs, LSTMs, and transformers across a wide suite of formal languages. Interestingly, RNNs and LSTMs generally perform better. Other interesting observations include (a) transformers can't learn Dyck-(2,3), as opposed to the results of Yao et al. (2021), and (b) the order of ranking between the different architectures is different from Deletang et al. (2023). The work emphasizes the need for empirical validations that align with theoretical results for a clearer understanding of neural network capabilities.

### Weaknesses
As such, the work doesn't have many weaknesses. I have a couple of questions regarding the setup.

a) **Behavior with input length**
- The authors report aggregated scores over strings of all lengths. It would be interesting to include a discussion on input length v/s performance for different models. Are there tasks where the transformer's performance shows a more exponential/drastic drop with input length?

b) **Tasks where additional loss terms hurt:** 
- Are there tasks where the additional language model loss and the next symbol loss hurt performance? For example, for parity, language model loss can intuitively hurt performance as the token at each step could be randomly selected for each string. 
- Furthermore, how do the optimal $\lambda$ hyper-parameters behave for different tasks for different models? Are there cases, where the additional losses help one architecture more than others?

c) **How is 64k parameters and 5 layers decided for the experiments?** What happens for smaller and wider models?

### Questions
Please check my questions in the above section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper takes a formal language theory approach to string classification and asks how well various types of neural networks recognize languages. The authors evaluate the network types on eighteen formal languages from three of the four languages classes of the Chomsky hierarchy (excluding recursively enumerable languages). Length generalization is tested systematically by using a short and a long validation set, and a test set that comprises much longer strings than in either validation set. They find that recurrent types of networks tend to be more accurate than transformers. The paper contains some analysis of certain languages on which one or more network types exhibits poor performance. The authors additionally describe an algorithm for efficiently sampling strings from a regular language that they describe as concurrent work.

--------

I will refer to the following papers in this review. [1] is relevant because the paper being reviewed here appears to be, at least in part, a response to [1]. [2] is relevant as an example of prior work with substantial overlap in experimental setting and possibly different results. [3] provides theoretical insights into the results reported in Section 4 of the paper reviewed here.

* [1] Neural networks and the chomsky hierarchy, Del{\'e}tang et al, 2023
* [2] MLRegTest: A Benchmark for the Machine Learning of Regular Languages, van der Poel et al, 2024
* [3] Why are Sensitive Functions Hard for Transformers?, Hahn & Rofin, 2024

### Strengths
This is a well-performed study of the ability of neural networks to recognize formal languages. The writing is of good quality, the methodology is clearly communicated, and it introduces an efficient algorithm for sampling strings from regular languages. Models are trained with validation sets of length [0, 40] (short) or [0, 80] (long) and tested on a set with strings of length [0, 500]. The authors of this study introduce several additional languages -- Dyck-(2, 3), binary strings that start with 1, and a distinction between marked and unmarked reversed strings -- that do not appear in [1]. The appendix contains copious information about the models trained.

### Weaknesses
* The general method for training neural networks as language recognizers is straightforward and is difficult to see as a substantial contribution (see similarities with e.g. [2]). Specifically, the novelty of applying this method to non-regular languages could be better highlighted. While the authors mention the generalization to any language with a sampling and membership testing algorithm, the practical implications and challenges of this generalization are not thoroughly discussed.
* The algorithm for efficiently sampling from a regular language, while interesting, seems to overshadow the core focus of the paper, which is the evaluation of neural networks on formal languages. The authors state that they use it for sampling training and evaluation instances from the regular languages (class `R` in Table 1). Since the algorithm is only used to generate data for 25% of the types of languages in this study, the amount of page real estate devoted to it seems disproportionate, particularly since algorithms for sampling from a formal language are not typically showcased in this venue. A more concise description of the algorithm, focusing on its unique aspects and how it differs from existing methods, would be beneficial.
* The insights about which languages are best-suited to which network types could be much deeper. With the literature on language recognition having advanced somewhat, reports that explain *the why* (e.g. [3]) are more compelling than those that describe *the what*. The results reported here are similar to [1] on the modular arithmetic language and marked string reversal and differ from [1] on cycle navigation. Some analysis is done here to characterize the kinds of errors transformers make on the task of recognizing strings from the cycle navigation language. The authors describe how with cycle navigation the recognition error of the instances with the highest cross entropy loss is always due to the model recognizing an instance with an incorrect final character (the position in the cycle). Since [1] reports 100% transduction accuracy for cycle navigation for RNN and LSTM, and 62% for a transformer, what explains the ceiling on recognition accuracy for all networks here? This discrepancy warrants further investigation. The analysis of Dyck-(2, 3) and Repeat 01 seems to primarily indicate that, with transformers,  some negative instances are near the decision boundary to positive instances. More insights about *why* this occurs with transformers and not the other networks would improve the paper. For instance, exploring the relationship between the sensitivity of these languages and the performance of transformers, as suggested by [3], could provide valuable insights.

Nit
* The standard deviation of recognition is a figure of merit for distinguishing neural network types, particularly in cases when no network achieves perfect recognition accuracy. This is included in the appendix. It would be helpful to report in Table 2 mean and stdev of recognition accuracy across multiple runs using the model from the appropriate table in the appendix.

### Questions
1. Can you clarify the contribution of this work in light of previous work on language recognition with neural networks? For instance, the authors of [2] have evaluated with larger datasets and have trained many more models. How does your contribution differ in terms of language classes tested and insights derived therefrom? Are there other aspects of your work that can be highlighted?
2. Have you considered investigating the scaling properties of the neural networks on the language recognition task? [1] demonstrated that none of the networks in your study are able to perform transduction on recursively enumerable languages without the support of an external memory module (e.g. Stack-RNN or Tape-RNN), but -- with respect to scaling -- only showed that increasing the amount of training data when the network is large enough to memorize the training data did not help generalization for some neural network types. Related: do you have any reason to believe that results you report here that differ in order from e.g. [1] -- such as recognition on cycle navigation -- are not due to the capacity of the network? Would larger networks recognize cycle navigation better?

### Soundness
4

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
This paper argue that there exists a methodological disconnect between the complexity theory of the formal language and the empirical evaluation of neural networks' computational capabilities. The existing work related the capabilities of neural networks with Chomsky hierarchy, which is framed in terms of language recognition (classifying whether strings belong to a language). However their empirical studies evaluate models on string-to-string transformation tasks instead. This paper propose an experimental setup for training neural networks as recognizers, and a more efficient algorithm for length-controlled sampling from finite automata. The empirical results show that RNNs and LSTMs often perform better than transformers on the formal language recognition task.

### Strengths
1. It is an important direction to study neural networks' computational ability through formal language theory.
2. This paper introduces an efficient algorithm for length-controlled sampling from finite automata, which may have practical value for future research in formal language processing.
3. Experiments are conducted on a variety of formal languages with 3 neural models with different architectures (RNN, LSTM, transformer). The methodology appears to be well-documented and reproducible.

### Weaknesses
1. The paper overlooks significant existing work on training neural networks for formal language recognition tasks (e.g. [1, 2, 3]). This oversight diminishes the claimed novelty of the proposed experimental setup. The authors should acknowledge and position their work in relation to previous studies. Specifically, the paper fails to adequately address how its approach differs from existing methods in terms of training objectives, negative sampling strategies, and the range of languages considered. For example, while the paper introduces a new sampling algorithm, it does not clearly articulate why existing sampling methods are insufficient for the task at hand, or how the proposed method offers a significant advantage beyond computational efficiency.
2. The claimed technical improvement in sampling from finite automata appears to be the main novel contribution, but its significance needs better contextualization. The paper does not sufficiently demonstrate the practical impact of this improvement. It is unclear how this new sampling algorithm enables the exploration of new research questions or leads to more robust conclusions about the capabilities of neural networks. The paper needs to provide more concrete examples of how the proposed sampling method overcomes limitations of existing approaches and enables new experimental designs.

### Questions
Please refer to the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper builds on Deletang et. al. 2023, and rigorously tests standard sequence neural architectures for their ability to _recognise_ formal languages that span the Chomsky Hierarchy. It also proposes a way to sample sequences from automata with a length constraint in order to generate training data for the experiment.

### Strengths
The paper references important work on the theoretical expressibility of Transformers, and other neural architectures, and, along with Deletang et. al. 2023, is useful information for understanding the learnability of these architectures in an empirical way.

It follows a similar set of experiments as the Deletang et. al. 2023 paper, while focusing on the recognition aspect of formal languages, rather than mixing recognition and transduction tasks. This of course comes with some drawbacks (e.g. uninformative training signal), but the authors spend some time addressing that issue with other reasonable auxiliary losses.

The length-constrained sampling from DFAs is an interesting aspect, even if it takes a bit of a detour from the original point of the paper

Understanding the limitations of the neural architectures we use is important, and can only be explored and understood in smaller scale experiments lik

### Weaknesses
I have only minor comments here as I find the paper well-executed:
- Table 2: decide on a threshold and make results above it visually dissimilar, this will give a better idea of where a model sits on these benchmarks and the hierarchy they’re measured to be in
- Missing a more conclusive figure regarding placement of models wrt to their level in the chomsky hierarchy. I know this is a tough ask, since the mapping of these models don’t fit as neatly into the Chomsky hierarchy as Deletang, et. al. 2023 suggest. Perhaps a better visual representation could be figured out.

### Questions
Can the length constrained algorithm for DFAs be modified for other automata? I suspect not due to the combinatorial way the paths compose for these other automata, and the infinite nature of the stack, etc.

### Soundness
4

### Presentation
4

### Contribution
3

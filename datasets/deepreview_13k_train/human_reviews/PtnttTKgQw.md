# Leaving the barn door open for Clever Hans: Simple features predict LLM benchmark answers

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
The integrity of AI benchmarks is fundamental to accurately assess the capabilities of AI systems. The internal validity of these benchmarks---i.e., making sure they are free from confounding factors---is crucial for ensuring that they are measuring what they are designed to measure. In this paper, we explore a key issue related to internal validity:~the possibility that AI systems can solve benchmarks in unintended ways, bypassing the capability being tested. This phenomenon, widely known in human and animal experiments, is often referred to as the `Clever Hans' effect, where tasks are solved using spurious cues, often involving much simpler processes than those putatively assessed. Previous research suggests that language models can exhibit this behaviour as well. In several older Natural Language Processing (NLP) benchmarks, individual $n$-grams like ``not'' have been found to be highly predictive of the correct labels, and supervised NLP models have been shown to exploit these patterns. In this work, we investigate the extent to which simple $n$-grams extracted from benchmark instances can be combined to predict labels in modern multiple-choice benchmarks designed for LLMs, and whether LLMs might be using such $n$-gram patterns to solve these benchmarks. We show how simple classifiers trained on these $n$-grams can achieve high scores on several benchmarks, despite lacking the capabilities being tested. Additionally, we provide evidence that modern LLMs might be using these superficial patterns to solve benchmarks. This suggests that the internal validity of these benchmarks may be compromised and caution should be exercised when interpreting LLM performance results on them.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates an interesting question about the validity of benchmarks for existing AI research -- whether simple n-gram features can solve these benchmarks. They train logistic classifiers to extract these text features and use them to predict results on multi-choice questions. The experimental results suggest that many existing benchmarks leak with these n-gram features, and potentially limit the validity of benchmarks. 
Furthermore, they test whether LLMs' predictions are based on these features. Their results show moderate evidence for the claim that models from OpenAI, Meta, Mistral AI, and Writer are more likely to provide correct answers for instances that n-gram models also successfully predictions.

### Strengths
The paper focuses on an important and timely issue of LLM evaluation -- whether the existing benchmarks are trivial and can be solved by simple text features, and furthermore whether LLMs rely on spurious cues to make correct predictions. 
The motivation and the related work survey across different disciplines are good, providing a basis for future research. 
The results of existing benchmarks that can be solved by simple text features are interesting.

### Weaknesses
The main weakness of this paper is the depth and comprehensiveness of empirical results. 
The paper investigates an important question and attracts me in the introduction. However, the empirical results are disappointing. For example, the authors show that text features can solve these benchmarks. What's next? Which dataset is the easiest to solve or leak? What's your advice to improve these datasets? What happens if a more controlled dataset is used to test the same capability? 

In addition, the authors need to provide more comprehensive results about how LLMs interact with these benchmarks. 
Your experiments on LLMs' prediction show only moderate evidence that these features are used. Does it indicate that the leaked information is not used? If so, does it effectively lower the importance of this research? 

Overall, I think the paper is not well-balanced with a big motivation and limited empirical results to support their motivation. 

Missing reference: 
Yan, Jianhao, et al. "Understanding In-Context Learning from Repetitions." The Twelfth International Conference on Learning Representations.

### Questions
If a dataset can be predicted by text features, does it mean that the tested capability can be bypassed? 
Furthermore, how does a tested capability differ from identifying the word usage?

### Soundness
2

### Presentation
2

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
This paper focuses on exploring the "Clever Hans" effect, also known as the "shortcut learning" effect, in which the trained model exploits simple and superficial correlations instead of intended capabilities to solve the evaluation tasks. The authors demonstrate that simple classifiers (logistic regression) trained on unigrams and bigrams can potentially predict correct answers in several benchmarks. They also provide evidence suggesting that some LLMs may rely on these simple patterns to achieve high performance, potentially undermining the validity of the modern LLM benchmarks.

### Strengths
- The motivation is clear and interesting. Focusing on superficial correlations of existing benchmarks can help benchmark design and evaluation for LLMs.
- The methodology of using logistic regression to analyze n-gram features across multiple benchmarks provides a clear and easy way to evaluate the quality of test datasets.

### Weaknesses
 - While the paper suggests that LLMs might be using n-gram patterns to solve benchmarks, it does not establish causality. It can be helpful to add experimental manipulation to directly test whether LLMs rely on n-grams.
- The findings may not apply universally across all LLMs or benchmarks, as the analysis is limited to specific datasets and model families. And based on the experimental results, only some families of LLMs demonstrate the possibility of relying on spurious correlations.
- The study focuses on a specific type of shortcut (n-grams) and may not capture other forms of spurious correlations that LLMs could exploit.

### Questions
Please see the weaknesses above.

### Soundness
2

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
2

### Summary
The paper examines multiple-choice benchmarks by training classifiers on various surface-level features, such as n-grams. This approach demonstrates that current evaluations may be susceptible to these spurious cues. The authors then use these classifiers to assess whether the performance of current models relies solely on surface-level features.

### Strengths
- The classifier approach presented in the papers is highly compelling for identifying whether spurious features (i.e n-grams features) exist in an evaluation.
- Meta-studies on evaluations offer an interesting and valuable research direction for the field.

### Weaknesses
 - The results show that certain LLMs performance correlates with performance on spurious (e.g., n-gram) features. However, there could be other features the models rely on to achieve similar performance to these classifiers. To address this concern, it might be helpful to include case studies on these data points to gain a qualitative understanding of the specific behaviors. Such case studies/analyses would be particularly convincing in demonstrating that LLMs exhibit this behavior. As currently presented, the paper may benefit from additional evidence to clarify the extent to which these spurious features influence LLM performance. Although the authors even concede this point in section 5.2, for which I am grateful to the authors, I do think this evidence is required for a more compelling case for why the community should care about these types of spurious features in evaluation.
- The method due to its reliance on n-gram is limited to multiple-choice questions. It would be more compelling if different types of methods could be constructed for other types of evaluations, such as open-ended QA.

### Questions
- What was the criteria for the datasets chosen, it would be interesting to include MMLU?

### Soundness
3

### Presentation
3

### Contribution
3

# Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 5, 5, 10

## Abstract
Large Language Models (LLM) are already widely used to generate content for a variety of online platforms. As we are not able to safely distinguish LLM-generated content from human-produced content, LLM-generated content is used to train the next generation of LLMs, giving rise to a self-consuming training loop. From the image generation domain we know that such a self-consuming training loop reduces both quality and diversity of images finally ending in a model collapse. However, it is unclear whether this alarming effect can also be observed for LLMs. Therefore, we present the first study investigating the self-consuming training loop for LLMs. Further, we propose a novel method based on logic expressions that allows us to unambiguously verify the correctness of LLM-generated content, which is difficult for natural language text. We find that the self-consuming training loop produces correct outputs, however, the output declines in its diversity depending on the proportion of the used generated data. Fresh data can slow down this decline, but not stop it. Given these concerning results, we encourage researchers to study methods to negate this process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper empirically investigates the self-consuming training loop in GPT-style models. To unambiguously verify the correctness of LLM-generated content, the authors propose to use logic expressions, as opposed to natural language, to construct the training dataset. The authors conducted comprehensive experiments with four distinct data cycles, and the generated content is evaluated in terms of both correctness and diversity. The experimental findings reveal that utilizing the model's own generated data leads to a decline in diversity.

### Strengths
This paper tries to reveal a critical issue in the data construction of LLMs, given the extensive use of WEB data and the challenges in distinguishing LLM-generated content from human-produced content. The authors conduct comprehensive experiments to explore the potential risks associated with directly feeding LLM-generated content into models, highlighting the limitations and risks of the self-consuming training loop.

### Weaknesses
Regarding the sampling methodology and synthetic content: The experimental setup deviates significantly from real-world LLM pretraining scenarios. In practice, the vast majority of pretraining data for open-sourced LLMs originates from human-written sources such as books and web pages. Even when synthetic content is utilized, it is often generated in diverse styles (e.g., textbooks, QA) based on existing human-written web content, rather than being directly sampled from LLMs for training purposes. The authors are encouraged to consider incorporating more realistic data sources and synthetic methods to enhance the practical relevance of their findings. Specifically, the direct iterative use of model outputs for subsequent training cycles, without any intermediate human-authored data or data augmentation, is a highly artificial scenario that does not reflect current pretraining practices. This raises concerns about the generalizability of the observed diversity decline to more realistic settings.

Concerning the logic expression dataset: While constructing datasets based on logic expressions facilitates the verification of content correctness, it also oversimplifies the underlying problem. The authors should consider the potential impact of the diversity and complexity of logic expressions on the experimental outcomes when designing their experiments. This could involve exploring the use of more complex logic expressions, such as those involving nested quantifiers or higher-order logic, or incorporating elements of natural language to better reflect real-world scenarios. The current use of relatively simple logic expressions might not fully capture the nuances of semantic drift that could occur in natural language text. Furthermore, the limited vocabulary and syntactic structure of the logic expressions may artificially constrain the diversity of the generated content.

Regarding the base model: It is recommended that the authors conduct additional pretraining using existing open-sourced LLMs, incorporating model-generated content to further enhance the practical relevance and generalizability of their findings. The use of a randomly initialized model, while providing a clean experimental setup, does not reflect the pretraining process of large language models, which typically involves extensive training on massive datasets. This discrepancy makes it difficult to assess the real-world implications of the self-consuming training loop on models that have already acquired a broad range of knowledge and linguistic abilities.

### Questions
How do the initial complexity and diversity of the logic expression datasets influence the final conclusions drawn from the experiments? It would be beneficial to explore the sensitivity of the results to variations in these factors.

If the new dataset is synthesized by referring to the original dataset, rather than being directly sampled from LLMs, would the diversity of the final output still exhibit a decline? This question aims to investigate the potential impact of different dataset synthesis methods on the diversity of the generated content.

### Soundness
2

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
3

### Summary
In this article, the authors design a series of experiments to explore the impact of self-consumption training loops on
large language models, in which the authors use Levenshtein diversity as an evaluation metric for data correctness and
diversity. Through the experiments, the authors argue that training a large language model using data generated by the
large language model leads to a decrease in the correctness and diversity of expression of the model, and analyze the
corresponding challenges of current large language model training.

### Strengths
1、 The effects of different data self-recycling methods, different model sizes, and the number of model iterations on language models
are compared in detail.
2、 Levenshtein diversity is used as an evaluation index of data correctness and diversity.
3、 The harm of the phenomenon is analyzed.

### Weaknesses
1. The literature: “AI models collapse when trained on recursively generated data” in the recursive data fine-tuning language
model has given the corresponding experimental proof of the phenomenon of the collapse of the language model and the
conclusion. It is not the case, as stated in the introduction, that only the use of recursive language training in the image
domain leads to model collapse. This paper explores the effect of data self-recycling on training in the non-fine-tuning case
from a different perspective, with limited innovation.
2. Levenshtein diversity has long been applied to measure text diversity, and is not considered NOVEL.(Ref:Beijering, Karin,
Charlotte Gooskens, and Wilbert Heeringa. "Predicting intelligibility and perceived linguistic distance by means of the
Levenshtein algorithm." Linguistics in the Netherlands 25, no. 1 (2008): 13-24.)
3. The number of model parameters used in the experiment is low and the type of data used is single, so the relevant
conclusions obtained are not rigorous.

### Questions
1. It is recommended that “output” be specified in Algorithms 1 and 2 to enhance the overall readability and comprehensibility.
2. The literature: “AI models collapse when trained on recursively generated data” has given corresponding experimental proofs
and conclusions on the phenomenon of recursive data fine-tuning of language models leading to the collapse of language models.
We hope that the authors will adjust the content of the article so as not to mislead the readers.
3. Figure 3 shows that using complete synthetic data to train the NGL model does not produce error data, while mixing artificial
data with synthetic data produces syntactically incorrect outputs, why is that?
4、 It is suggested to give the formula of the indicator ' Average Normalized Levenshtein Distance ' to make it easier for readers to
understand.
5、 Using logic expressions as training data does have some unique advantages in evaluating the semantic correctness of the
output of a language model, but there are differences between this kind of data and real textual data, and I'm curious how the
semantic correctness and variety of outputs in the article would be reflected on real textual data?

### Soundness
3

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
This paper presents an initial study of the influence of self-consuming style training on the generation quality of LLMs. A logic expression dataset is used to avoid the inaccurate measurement of generated text quality or diversity.  In the evaluation part, four types of self-consuming training are incorporated to comprehensively compare the effect of self-generated data.

### Strengths
* This paper studies an interesting question, which is a valuable contribution to the further development of LLM and a deeper understanding of self-consuming training.
* The paper is well-written and easy to follow.

### Weaknesses
 * The author missed a series of related works on self-consuming training (self-training) of LLM, and here are some examples [1][2][3].

* The experiment setup is not convincing to me. The generation quality is not equivalent to the correctness of the generated logic expression. Therefore I don't think the evaluation successfully reflects certain properties of self-training of LLMs. 

* Logic expressions merely form a small part of data that LLMs can generate. Experiments with only logical expressions cannot lead to a general conclusion, for instance, self-training in LLM may or may not result in XXX.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors test whether the re-use of already-generated examples from an LLM in further pre-training of the same model result in lower quality output. They measure the output in two ways: correctness and diversity. They use a clever, if somewhat limiting, approach to automatic evaluation: teaching the model to generate logic statements which evaluate to `True`, e.g., by the Python `eval` command, allowing them to evaluate correctness easily. To evaluate diversity they examine the number of unique statements generated as well as their diversity, measured using the Levenshtein Diversity, an averaged, normalized Levenshtein distance between all pairs of generated statements. Within this framework, they show that the re-use of previously generated statements as further training data invariably makes the model more "correct" in the sense that it generates only True statements, but also that the diversity inevitably suffers, in the most extreme cases to the point that the model generates only one output. Diversity begins to fall dramatically before the outputs become truly non-unique.

### Strengths
The problem is very clearly framed and good background from the similar problem in image generation is helpful. The author's approach to make a tractable experiment by using logic statements is quite clever, and makes it easy to understand the impacts of "self-consuming" training. The authors present a solid range of experiments, focusing on generations of self-consumption, different degrees and styles of self-consumption, and--in the appendices--model size. The results are stark and convincing, at least in the context of the logic statements they evaluate.

### Weaknesses
The authors are aware of some of the limitations of the work--it is possible to claim that a sufficiently large model might not suffer from these problems, but the authors have made a good attempt to address this up to a certain scale, and as they point out the cost (both in dollars and CO2) of such an experiment at large scale would be prohibitive and probably unethical. A more subtle limitation might be that the range of language tested in this paper is necessarily quite small. It would be interesting to extend the experiments to a larger language, perhaps something like SQL which is still easily verified but has a richer vocabulary. The use of logic statements, while clever for automatic evaluation, inherently limits the complexity and diversity of the generated text. This raises questions about the generalizability of the findings to more complex natural language tasks where the relationship between correctness and diversity might not be as straightforward. The study also does not explore the impact of different pre-training data distributions on the self-consumption phenomenon. It is possible that the observed effects are specific to the type of data used for initial pre-training, and that different pre-training data could lead to different outcomes when the model is trained on its own generated outputs.

### Questions
My main suggestion is to try this work with a more sophisticated but still machine-evaluatable language, such as SQL. This is a harder problem, but one with probably more diversity, and it might help in making the results more robust to any criticism that the language was too simple. I realize that would be difficult or impossible to do for this submission, but it would make the work stronger.

### Soundness
4

### Presentation
4

### Contribution
4

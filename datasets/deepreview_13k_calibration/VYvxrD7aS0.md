# ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
Language models (LMs) have become a staple of the code-writing toolbox. Their pre-training recipe has, however, remained stagnant over recent years, barring the occasional changes in data sourcing and filtering strategies. In particular, research exploring modifications to Code-LMs' pre-training objectives, geared towards improving data efficiency and better disentangling between syntax and semantics, has been noticeably sparse, especially compared with corresponding efforts in natural language LMs. In this work, we examine grounding on obfuscated code as a means of helping Code-LMs look beyond the surface-form syntax and enhance their pre-training sample efficiency. To this end, we compile ObscuraX, a dataset of approximately 55M source and obfuscated code pairs in seven languages. Subsequently, we pre-train ObscuraCoder models, ranging in size from 255M to 2.8B parameters, on a 272B-token corpus that includes ObscuraX and demonstrate that our obfuscation-based pre-training recipe leads to consistent improvements in Code-LMs' abilities compared to both vanilla autoregressive pre-training as well as existing de-obfuscation (DOBF) objectives. ObscuraCoder demonstrates sizeable gains across multiple tests of syntactic and semantic code understanding, along with improved capabilities in multilingual code completion, multilingual code commit summarization, and multi-purpose library-oriented code generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a pre-training strategy that relies on code obfuscation to help models disentangle the semantics and syntax of code during pre-training. Obfuscation is applied to function names, variable names, import statements as well as package names. Some of the details were unclear (especially on the masking applied) but it appears that, given a source code snippet the pretraining data may see the source code as-is (as in regular CausalLM), the source code with function name obfuscation or pre-training with bi-directional obfuscation translation data. In contrast, DOBF a baseline method of obfuscation uses a obfuscated code along with identify maps or regular source-code. Data used for pre-training includes mixed-medium data (code + text) (90B tokens) as well as source-code only data (152B tokens) in the first phrase along with 30B of randomly-shuffled (code+text). In the second phrase, they use 30B tokens of obfuscated code, 58B tokens of obfuscation translation (bi-directional),  and a randomly shuffle of code+text for 30 B tokens. Models are primed with text only before source code is introducted in pre-training. Evaluations presented are presented at different model scales (255M - 2.8B) all with a fixed data budget of 272B tokens. In contrast to using the regular CausalLM training, they report a gain across all metrics on tasks of defect detection, code completion and library oriented code generation. In contrast to DOBF (which appears to be better than vanilla CausalLM), the method still does better. 

Overall a good, well documented paper.

### Strengths
- Interesting use of code-obfuscation
- Well constructed experiments to help answer the empirical questions posed
- Dataset shall be released after paper publication

### Weaknesses
 - While the goal of the work was to demonstrate the benefit of code obfuscation (motivated in trying to separate semantics and syntax to improve code-understanding), it would have been helpful to have at least one baseline from the related work in Lines 147-157. At the moment its unclear how one should act on the findings in the paper or how they compare with other approaches (that share the same motivation but are not obfuscation based).



### Questions
1. See Weakness. Would it be possible to study this at the smallest scale if there's training budget (and adequate time) during the rebuttal?
2. The motivation for obfuscating library and names and package names was a bit counter-intuitive to me. Wouldn't we want the model to *learn* different package names and what they do? I note the results presented in 391-409 but I am not sure I'm convinced that specifically this type of obfuscation could explain the gain? To make this claim, wouldn't you need to pretrain without this type of obfuscation present?

### Soundness
3

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
4

### Summary
This paper proposes a pre-training objective for code language models (Code-LMs) that leverage obfuscated code. The authors claim that "grounding" Code-LMs on obfuscated code helps to disentangle syntax and semantics, which is essential for improving their performance on downstream tasks such as code defect detection, library-oriented code generation, and multilingual code completion.

However, there is a large line of missing literature, mostly on natural language processing and machine learning, that discusses training neural networks to disentangle syntax and semantics in natural language, and some of them even deal with code. In my opinion, the authors should have discussed these papers in more detail and compared their work with them.

Disclosure: my related expertise is more on the machine learning and language modeling side, as well as the related (computational) linguistics perspective. I am not very familiar with the large body of software engineering literature this paper has cited, nor can I evaluate whether the paper has made a significant contribution to the area of SE. However, since ICLR is more considered a machine learning conference, my evaluation is provided from the perspective of machine learning.

### Strengths
- The idea is well presented, and the paper is generally easy to follow. All research questions are stated and, to some extent, well answered. A comprehensive ablation study is conducted.
- A promising code model will be released.

### Weaknesses
 - The authors' background may be more on the software engineering side---most of the cited work is on software engineering, and there is a significant line of literature missing in machine learning and natural language processing.

    In terms of disentangling syntax and semantics, the following two papers discuss training neural networks to disentangle syntax and semantics in natural language:
    - https://aclanthology.org/N19-1254/
    - https://aclanthology.org/P19-1602/

    In terms of semantic-aware language/code generation with language models, the following papers are very relevant:
    - (natural language) https://aclanthology.org/2021.emnlp-main.564/
    - (code) https://aclanthology.org/2022.emnlp-main.231/
    I especially wonder how the performance of the proposed method compares to other models with the decoding strategy proposed in this paper.

    In training code models, the following ICLR 2023 paper is worth comparing to:
    - https://openreview.net/forum?id=hQwb-lbM6EL

    Related to library-oriented code generation, the following ICLR paper is worth referencing:
    - https://openreview.net/forum?id=ZTCxT2t2Ru

- I'm not sure if this comes from the cross-domain difference: to me, with backgrounds in machine learning and linguistics, both syntax and semantics of the original and obfuscated code shown in Figure 1 are all the same. The difference comes from the lexical-level symbols (i.e., variable and function names); therefore, the approach does not really disentangle syntax and semantics but rather disentangling form and meaning. I believe there would be a large amount of ICLR audience who would think the same.

- While the main performance in Table 1 is promising, it is not sufficient to demonstrate the effectiveness of the proposed method. On BigCodeBench, the model performs much worse than most existing models (except StarCode) with a comparable number of parameters Pass@1. Given that DOBF (Lachaux et al., 2021) has already been introduced, I would expect the performance of the proposed model to be better in order to demonstrate enough contribution.

### Questions
1. It is not very clear to me what the authors mean by "grounding," which has already been an overloaded term in the machine learning community (cf. Chai et al., 2018). Can the authors provide a more detailed explanation of what they mean by "grounding" in the context? Is this a software engineering term?

[Chai et al., 2018] https://www.ijcai.org/Proceedings/2018/0001.pdf

2. L397: have you tried evaluating Pass@1 with greedy decoding (i.e., temperature = 0)? Since you are anyway submitting one prediction for testing, I would expect greedy decoding generating a program with higher probability (assigned by the model).

3. Table 1: the metrics of ReCode are never introduced in the paper. Please add a brief explanation of what the metrics are.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ObscuraCoder, an approach to enhance the pre-training of Code-LMs by focusing on the disentanglement of syntax and semantics through the use of obfuscated code. Traditionally, Code-LMs rely on autoregressive pre-training which often struggles to handle semantic-preserving syntactic perturbations, thereby reaching a plateau in terms of data efficiency and model robustness. To address these challenges, the authors propose grounding the pre-training on a dataset called ObscuraX, which comprises approximately 55 million pairs of source and obfuscated code across seven programming languages. This method contrasts with previous efforts such as DOBF, which primarily aimed to revert obfuscated code to its original form. ObscuraCoder, ranging from 255M to 2.8B parameters, is pre-trained on a substantial 272B token corpus, including ObscuraX. It achieves significant improvements in syntactic and semantic understanding of code, surpassing both conventional autoregressive pre-training and DOBF models. Notably, ObscuraCoder facilitates enhancements in multilingual code completion, commit summarization, and versatile library-focused code generation, without necessitating modifications to the Code-LM during inference.

### Strengths
1. The evaluation of this paper is exceptionally solid:
    1. ObscuraCoder is benchmarked against strong well-established models such as DeepSeekCoder and StarCoder. Those models are very strong at 1B scale, ensuring a competitive comparison.
    2. The model is trained across four different sizes, showing its scalability.
    3. Controlled experiments provide a fair comparison by training ObscuraCoder and baseline models (CausalLM and DOBF) under the same conditions across all scales, attributing its good performance to the proposed methods rather than discrepancies in training setups.
    4. A comprehensive selection of benchmarks is used for evaluation, covering a broad spectrum of tasks across large, multilingual datasets.

2. ObscuraCoder consistently surpasses baseline models in a variety of tasks and scales, with performance gains increasing with model size. This showcases both the effectiveness of the deobfuscation pretraining and its scalability.

### Weaknesses
1. The methodology of ObscuraCoder closely resembles the DOBF, which slightly diminishes the novelty of the paper. However, the scope and depth of the experiments and evaluations presented significantly exceed those found in prior DOBF studies.

2. The quality of the pretraining data is not sufficiently controlled in the experiments:
    - The ObscuraX dataset has been curated using Tree-Sitter to drop non-parsable code, and contain more self-contained code. So it contains higher-quality, cleaner code compared to other corpora.
    - Only ObscuraCoder is trained with the higher-quality ObscuraX, whereas the CausalLM and DOBF models are not, raising concerns that performance gains might be attributed to dataset quality rather than the training objective.
    - To verify the effectiveness of the deobfuscation objective, the authors could:
        1. Develop a non-obfuscated version of ObscuraX.
        2. Pretrain a CausalLM using this dataset (mixed with other datasets used by ObscuraCoder, except obfuscated ObscuraX)
        3. Compare its performance against ObscuraCoder to conclusively attribute any improvements to the deobfuscation objective.

3. The paper lacks comprehensive discussion on related works that are highly relevant:
    - While CodeT5 (https://arxiv.org/abs/2109.00859) is mentioned in this paper, CodeT5 actually uses an "identifier-aware" pretraining objective related to code obfuscation. Those pertinent details are not discussed in this paper.
    - AST-T5 (https://arxiv.org/abs/2401.03003), another model trained with syntax-aware objectives and known for its code translation capabilities, should also be included in the related work section.

4. The writing style of the paper, particularly in the abstract and introduction, could be simplified. The use of overly complex vocabulary may hinder understanding of the content.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ObscuraX and ObscuraCoder, respectively a novel dataset and model for the code LM domain, based on the premise that current approaches to training code language models do not sufficiently take into account the inherent differences in syntactic and semantic structure between programming and natural languages.

Starting from the observation that current data approaches tend to focus on scaling, which may in the near future lead to a data bottleneck, but not on disentangling/making available for learning the syntactic and semantic aspects of modern high-level programming languages, the authors propose a code obfuscation training paradigm, and set out to answer a number of interesting research questions:
1) Does their paradigm lead to improvements on tasks requiring code syntax/semantic understanding?
2) Does obfuscating imports improve library use?
3) Is there any performance regression associated with obfuscation training?
4) How does model performance scale under the proposed training paradigm?

To this end, they lay out in detail how their ObscuraX dataset was created (including code obfuscation, part of which includes obfuscating library import and use), and how their ObscuraCoder models are subsequently trained.\
ObscuraX consists of a large collection of code data scraped from the web; contrary to previous work which uses some code obfuscation as a translation target, the authors introduce a mix of 4 pretraining "objectives": (1) translating original code to obfuscated code; (2) translating obfuscated code to original code; (3) CLM training on original code; (4) CLM training on obfuscated code.

Extensive evaluations against the same model architecture (Llama) on data of comparable size and from the same sources trained as "classic" causal LM (i.e., original code only) indicates that the proposed mixed objective pretraining provides meaningful signals related to syntactic and semantic understanding to the model, improving performance on all evaluated tasks.\
In some conditions, the proposed ObscuraCoder models can even compete with or outperform current frontier models, which are often much larger or trained on at least an order of magnitude more data.\
Comparison to a DOBF-inspired decoder-only model also indicates perfomance gains over using code-to-obfuscation translation as the only added pretraining objective.

### Strengths
The paper is very well written and presented. It was very easy to follow, and the authors very clearly laid out the objectives and research questions they want to address.

The paper does an excellent job explaining the data collection and model training methodology, and the provided experiments are meaningful in addressing the posed research questions.

The performance of models trained on the proposed novel obfuscation-grounded dataset indicate that the authors are onto something, and that the proposed training paradigm is meaningful and effective.

### Weaknesses
There are some strong claims made about the benefits of the proposed dataset, without testing these by ablating the corpus.
In particular, RQ2 asks whether obfuscating library imports improved model performance, and is answered in the positive in Section 5; however, this assertion seems to be based on training on data using the full ObscureX obfuscation method, which includes library obfuscation (25%) as well as "standard" code obfuscation.

I am not sure this is a valid conclusion, as these results may as well stem from training on the obfuscated data in general, and not the library obfuscation in particular. It would have been more convincing to use an ablation here and train a model on a version of ObscureX that does not contain library obfuscation at all. This model could then be compared to the model presented here (trained on the full ObscureX data paradigm), to see if there is an improvement that can be specifically attributed to the introduction of library obfuscation.

To some extend this is indicated by the DOBF-based decoder model in Section 6; however, that model is trained differently, with backpropagation on the identifier maps only.

### Questions
I really like this paper, and how well-structured and principled it approaches its objective and research questions.

For questions, see my answer to "Weaknesses": Am I right that the shown ablation on DOBF only partially covers RQ2? I don't think it was intended as part of addressing RQ2, since it comes in a section after the main experiments. Did you (or could you?) train models that use ObscureX data that has not gone through library import obfuscation? That would show better if that particular obfuscation method yields additional performance gains past "standard" code obfuscation.

Otherwise, there are just some typos/minor things I noticed during reading:
- Figure 1: The "FUNC_0" on the translation side (purple) of DOBF should be "def"?
- Line 185: "Other work work"
- Line 279: "confiscated code" -> obfuscated?
- Lines 316-317: "[...] as it is nearly an order of magnitude greater that what would be optimal according to the scaling-law." I do not understand this sentence, could you rephrase this?
- Line 518: "effectiveness of out obfuscation" -> our
- Line 522-523: "Unfortunately, we find that post-hoc obfuscation training does bring performance gains to causally pretrained LMs." -> pretty sure this should be "does *not* bring performance gains"?

### Soundness
3

### Presentation
4

### Contribution
3

# The Foundations of Tokenization: Statistical and Computational Concerns

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 8, 5, 5

## Abstract
Tokenization---the practice of converting strings of characters from an
  alphabet into sequences of tokens over a vocabulary---is a critical step in
  the NLP pipeline. The use of token representations is widely credited with
  increased model performance but is also the source of many undesirable
  behaviors, such as spurious ambiguity or inconsistency. Despite its recognized
  importance as a standard representation method in NLP, the theoretical
  underpinnings of tokenization are not yet fully understood. In particular, the
  impact of tokenization on statistical estimation has been investigated mostly
  through empirical means. The present paper contributes to addressing this
  theoretical gap by proposing a unified formal framework for representing and
  analyzing tokenizer models. Based on the category of stochastic maps, this
  framework enables us to establish general conditions for a principled use of
  tokenizers, and most importantly, the necessary and sufficient conditions for
  a tokenizer model to preserve the consistency of statistical estimators.
  Additionally, we discuss statistical and computational concerns crucial for
  designing and implementing tokenizer models, such as inconsistency, ambiguity,
  tractability, and boundedness. The framework and results advanced in this
  paper contribute to building robust theoretical foundations for
  representations in neural language modeling that can inform future empirical
  research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Disclaimer: I previously reviewed an earlier version of this paper during its submission to NeurIPS 2024.

This paper proposes a formal approach to tokenization. Specifically, the authors apply the notion of stochastic maps (Baez & Fritz, 2014) to tokenization models, which allows them to formalize key properties of tokenizers such as their consistency. In a next step, they use their framework to analyze further statistical and computational aspects of tokenization (e.g., spurious ambiguity).

### Strengths
The paper has several strengths:

- Tokenization is a critical aspect of modern-day natural language processing, but its theoretical underpinnings are not yet fully understood. The formalisms introduced in the paper help close this gap and might become the basis for future work.
- The application of stochastic maps to tokenization is novel.
- The presentation is excellent; the writing is clear and overall easy to follow.

### Weaknesses
This is a completely theoretical paper without any empirical evaluation. While not a weakness _per se_, the authors mention that their findings have implications for the practical use of tokenizers (e.g., line 95). Compared to the version of the paper that was under submission at NeurIPS 2024, the authors have added sections discussing practical aspects of their observations (e.g., lines 345-350), but I still believe that a proper case study showcasing the practical value of the proposed formal framework would greatly enhance the potential impact of the paper. This is particularly desirable since many of the discussed problems are well-known in the community, so it is not clear what exactly the paper adds beyond a new theoretical perspective. The lack of empirical validation makes it difficult to assess the real-world relevance and impact of the proposed formalism. While the theoretical framework is interesting, without concrete examples demonstrating its utility, it remains unclear whether it offers any practical advantages over existing tokenization methods. The paper would benefit from a more thorough discussion of how the proposed framework could be applied to solve specific problems in NLP, and what advantages it might offer compared to existing approaches. The current discussion of practical aspects is too high-level and lacks concrete examples.

While you mention the relation between tokenization and linguistic segmentation, you should give more credit to the line of work that has investigated this link over the last few years (e.g., [Bostrom & Durrett, 2020](https://aclanthology.org/2020.findings-emnlp.414/), [Hofmann et al., 2021](https://aclanthology.org/2021.acl-long.279/), [Gow-Smith et al., 2022](https://aclanthology.org/2022.emnlp-main.786/), [Beinborn & Pinter, 2023](https://aclanthology.org/2023.emnlp-main.272/)), which is also relevant for your discussion of linguistic ambiguities (lines 395-399). The paper does not adequately acknowledge the existing body of research that has explored the connection between tokenization and linguistic segmentation. This omission weakens the paper's contextualization and makes it appear as if the authors are not fully aware of the relevant literature. The discussion of linguistic ambiguities would be significantly strengthened by a more thorough engagement with these prior works.

Lines 405-410: I think you should mention that the practical benefit of this operation has been shown to be negligible in most cases ([Chirkova et al., 2023](https://aclanthology.org/2023.acl-short.1/)). The paper should acknowledge that the practical benefits of marginalization are often negligible, as demonstrated by prior work. This omission could lead readers to overestimate the practical value of this operation within the proposed framework. The authors should explicitly discuss the limitations of marginalization and its potential drawbacks in real-world applications.

I would recommend putting the examples from the appendix back into the main paper, especially Example 8.1. You have a bit of space left, so this should be feasible, and it would help illustrate your arguments.

Typos:
- Line 120: "distributions" -> "distribution"
- Line 158: "equation equation 1" -> "equation 1"
- Line 205: "this" -> "these"
- Line 459: "complexity a tokenizer model" -> "complexity of a tokenizer model"

### Questions
Comments:
- While you mention the relation between tokenization and linguistic segmentation, you should give more credit to the line of work that has investigated this link over the last few years (e.g., [Bostrom & Durrett, 2020](https://aclanthology.org/2020.findings-emnlp.414/), [Hofmann et al., 2021](https://aclanthology.org/2021.acl-long.279/), [Gow-Smith et al., 2022](https://aclanthology.org/2022.emnlp-main.786/), [Beinborn & Pinter, 2023](https://aclanthology.org/2023.emnlp-main.272/)), which is also relevant for your discussion of linguistic ambiguities (lines 395-399).
- Lines 405-410: I think you should mention that the practical benefit of this operation has been shown to be negligible in most cases ([Chirkova et al., 2023](https://aclanthology.org/2023.acl-short.1/)).
- I would recommend putting the examples from the appendix back into the main paper, especially Example 8.1. You have a bit of space left, so this should be feasible, and it would help illustrate your arguments.

Typos:
- Line 120: "distributions" -> "distribution"
- Line 158: "equation equation 1" -> "equation 1"
- Line 205: "this" -> "these"
- Line 459: "complexity a tokenizer model" -> "complexity of a tokenizer model"

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a formalization of the tokenization process in modern language models. The formalization is based on the category of stochastic maps, which presents a novel and unified framework for representing and analyzing tokenizers. The paper also provides some examples of sing the framework to account for tokenizer behavior such as ambiguity and inconsistencies.

### Strengths
The paper presents a novel framework for representing and analyzing tokenizers in the form of stochastic maps. The proposed framework has the potential to provide more a foundational statistical understanding of tokenizer behavior, which may lead to practical improvements.

### Weaknesses
The paper presents a novel framework for representing and analyzing tokenizers in the form of stochastic maps. The proposed framework has the potential to provide more a foundational statistical understanding of tokenizer behavior, which may lead to practical improvements.

The paper provides some examples of how the framework can be utilized to shed new light on tokenizer behavior such as ambiguity and inconsistency, but it is not immediately clear to what extent the proposed framework can lead to practical improvements of tokenizer performance. Specifically, while the formalism is interesting, the paper lacks a clear demonstration of how this framework can be used to address concrete problems in tokenization beyond the examples provided. The connection between the theoretical framework and practical applications is not sufficiently established, making it difficult to assess the real-world impact of the work.

### Questions
Would it be possible to provide some concrete examples of how the framework can be used to shed new light on differences between different types of tokenizers?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The authors address the problems of tokenization and use of the token representations in NLP from a foundational mathematical perspective. Based on the category of stochastic maps, the authors propose a general definition of a tokenizer as an arbitrary pair of composable maps, and this theoretical framework enables to establish general conditions for a principled use of tokenizers and the necessary and sufficient conditions for a tokenizer model to preserve the consistency of statistical estimators. The statistical and computational concerns (inconsistency, ambiguity, tractability, and boundedness) are discussed. To achieve this, authors characterize these known issues through the lens of formal properties of composable maps, such as injectivity, multiplicativity, and finite decomposition.

### Strengths
— Theoretical position paper is from a foundational perspective, and mathematically justified analysis is introduced; strict definitions and notation conventions are presented.

### Weaknesses
It's still unclear how to apply this knowledge to practical issues and better tokenizers for LLMs. The paper presents a theoretical framework using stochastic maps, but it does not sufficiently bridge the gap to concrete applications. While the authors define tokenizers as composable maps and discuss properties like injectivity and multiplicativity, the implications of these properties for real-world tokenizer design remain abstract. For example, the paper discusses the conditions for a tokenizer to preserve the consistency of statistical estimators, but it does not provide specific guidance on how to construct tokenizers that satisfy these conditions in practice. The discussion of ambiguity, tractability, and boundedness is also high-level and lacks concrete examples of how these issues manifest in existing tokenization methods and how the proposed framework can address them. The paper's focus on formal properties such as finite decomposition is interesting, but it's not clear how these properties translate into practical advantages for tokenization in LLMs.

### Questions
I am unsure if I am not a relevant reviewer for this paper or if the paper is too foundational for the conference.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates into the tokenization process for language modelling from a theoretical viewpoint. 

The framework examines language modelling as mapping between a true language model on an alphabet and a learned language model on a separate alphabet, known as a stochastic map. In section 3, the paper establishes convergence property for various distributions in different spaces, as well as necessary function properties (injectivity and surjectivity). Later on, the paper leverages such properties to examine the problems (e.g injectivity, surjectivity) of current language models and connect them with concrete issues such as inconsistency, ambiguity, tractability, etc.

### Strengths
The paper proposes an interesting and also promising theoretical direction to examine the tokenization problems: by explicitly examining the relationship between the true language model under its alphabet and the learned language model with the practical alphabet. Under this framework, the paper has shown some interesting preliimary results:
- Define propery the consistency from analysis viewpoint
- The propoerty of encoder and decoder and connect them with the problem of inconsistency and ambiguity

### Weaknesses
The connections between the derived properties/theorems and the NLP practice/problems are not strong. My arguments are stated as the following:
- In theorem 3.1 the authors derive the condition to make the estimator consistent; however, this property is nowhere more leveraged, the paper discusses in more detail the exact mappings and the derived injectivity/surjectivity properties which do not require the analysis from 3.1 and makes 3.1 a isolated construction without any implication built inside the paper.
- The injectivity (and surjectivity) discussions look more like discussions as a "related work" section. For example, no derivations are shown for problems such as "how severe the problem is when injectivity assumption is broken" or "when injectivity are ensured by certain techniques, what is the advantage quantified/bounded mathematically".
- While the boundness and tractability discussions are interesting, they are of observational nature. The paper will have significantly more impact if the paper is able to derive algorithms/improvements/theoretical implication out of them.

### Questions
Can the authors further clairify the connection between 3.1 and the rest of the paper please?

### Soundness
3

### Presentation
2

### Contribution
2

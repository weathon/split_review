# h4rm3l: A Language for Composable Jailbreak Attack Synthesis

- Decision: Accept
- Scores: 6, 8, 5, 8

## Abstract
Despite their demonstrated valuable capabilities, state-of-the-art (SOTA) widely
deployed large language models (LLMs) still cause harm to society due to the inef-
fectiveness of their safety filters, which can be bypassed by prompt transformations
called jailbreak attacks. Current approaches to LLM safety assessment, which
employ datasets of templated prompts and benchmarking pipelines, fail to cover
sufficiently large and diverse sets of jailbreak attacks, leading to the widespread
deployment of unsafe LLMs. Recent research showed that novel jailbreak attacks
could be derived by composition, however, a formal composable representation for
jailbreak attacks, which among other benefits could enable the exploration of a
large compositional space of jailbreak attacks through program synthesis methods,
has not been previously proposed. We introduce h4rm3l, a novel approach
addressing this gap with a human-readable domain-specific language (DSL). Our
framework comprises: (1) The h4rm3l DSL, which formally expresses jailbreak
attacks as compositions of parameterized string transformation primitives. (2)
A synthesizer with bandit algorithms that efficiently generates jailbreak attacks
optimized for a target black box LLM. (3) The h4rm3l red-teaming software
toolkit that employs the previous two components and an automated harmful
LLM behavior classifier that is strongly aligned with human preferences. We
demonstrate h4rm3l’s efficacy by synthesizing a dataset of 2656 successful
novel jailbreak targeting 6 SOTA open-source and proprietary LLMs (GPT-3.5,
GPT-4o, Claude-3-sonnet, Claude-3-haiku, Llama3-8b, and Llama3-70b), and
by benchmarking those models against a subset of the synthesized attacks, and
previously published jailbreak attacks which were used as few-shot examples. Our
results show that h4rm3l’s synthesized attacks are diverse and more successful
than previously reported attacks, with success rates exceeding 90% on SOTA LLMs.
Warning: This paper and related research artifacts contain offensive and
potentially disturbing prompts and model-generated content.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces h4rm3l, a domain-specific language (DSL) designed to formally represent jailbreak attacks on large language models (LLMs) as compositions of parameterized string transformations. The authors propose a framework that includes the h4rm3l DSL, a synthesizer with bandit algorithms for generating optimized jailbreak attacks, and a red-teaming software toolkit. The paper demonstrates the efficacy of h4rm3l by synthesizing a dataset of successful jailbreak attacks targeting six SOTA LLMs, showing higher success rates than previously reported attacks.

### Strengths
- This paper introduces the first formal, composable representation of jailbreak attack, providing a more systematic and comprehensive approach to assessing LLM vulnerabilities.
- The efficacy of the proposed framework is effectively demonstrated through the synthesis of a substantial dataset comprising successful jailbreak attacks against multiple state-of-the-art (SOTA) LLMs.

### Weaknesses
- The estimation of attack success rates relies solely on the assessment of 100 Claude-3-haiku responses by just two human annotators, which raises concerns about the generalizability of the findings.

- The relationship between various jailbreak methods and their impact on the results is not clearly articulated, particularly how the synthesis with h4rm3l connects to these outcomes.

- Some parts of the paper are vaguely written and are subject to elaboration and clarification.

- The following issues are subject to further clarification:
  - What do the numbers (e.g. "00536") in Figure 4 represent?
  - Are the horizontal and vertical coordinates of Figure 5 meaningful?
  - In line 928, "therefore we use proxy names" Do the proxy names here refer to the letters G, B and U?
  - What do the abbreviations BS, RP, and RT in Tables 3 and 4 signify?
  - In line 1222, "Table 2 and Table 3" should be corrected to "Table 3 and Table 4."?

### Questions
- What are the time and computational costs associated with using h4rm3l for synthesizing attacks?

### Soundness
2

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
3

### Summary
This paper introduces h4rm3l, a domain-specific language (DSL) for representing jailbreak attacks on large language models (LLMs) as compositions of parameterized string transformation primitives. The authors develop a synthesizer using bandit-based few-shot program synthesis to generate novel, high-success-rate jailbreak attacks against black-box LLMs. They demonstrate the effectiveness of h4rm3l by synthesizing 2,656 successful attacks targeting six state-of-the-art LLMs, achieving high success rates. The work also includes a zero-shot harmful LLM behavior classifier and an open-source red-teaming toolkit.

### Strengths
- The paper addresses a timely and relevant topic.
- The structure of the writing is clear and well-organized.
- The paper presents an innovative idea by transforming the jailbreak task into a formal language implementation.
- Implementing various existing jailbreak methods to support the proposed composite attack strategy.

### Weaknesses
- Unclear Motivation and Purpose: The motivation and unique advantage of transforming jailbreak tasks into a formal language are not entirely clear. In my view, directly developing a framework or tool that integrates multiple jailbreak prompting operators and scheduling strategies may already suffice for most jailbreak/red-teaming needs. Therefore, what specific advantages or unique capabilities does this formal language offer? How does it surpass the functionalities of traditional red-teaming frameworks? Additional clarification from the authors would be helpful.

- Assessment Method in Section 3.3: Using GPT as a judge has become a mainstream approach for evaluating jailbreak success rates, and many recent studies follow standard methods. However, this paper appears to introduce a new prompt. Is this prompt demonstrably superior to those used in other jailbreak studies? Alternatively, what necessary adaptations or unique design choices were made to tailor this prompt for the work presented here?

- Efficiency Comparison in Experiments: While the authors clearly present the effectiveness of the proposed method compared to baselines in jailbreak success rates (as shown in Fig. 4), a comparative analysis of jailbreak efficiency with existing methods is lacking. Figures 2 and 3 only show the number of iterations required by the proposed method. I suggest the authors provide a more straightforward and detailed efficiency comparison with baseline methods.

### Questions
1. Compared to directly building a red-teaming framework, what are the unique advantages of the formal language proposed in this paper?
2. Does the proposed jailbreak attack demonstrate superior efficiency compared to the baselines discussed in the paper?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces h4rm3l, a novel approach to cover sufficiently large and diverse sets of jailbreak attacks with human-readable domain-specific language. h4rm3l includes (1) a domain-specific language formally expresses jailbreak attacks as compositions of parameterized string transformation primitives, (2) a synthesizer with bandit, and (3) a red-teaming software toolkit. h4rm3l also provides a dataset of 15891 novel jailbreak attacks and safety benchmarking results for 6 SOTA LLMs with 82 jailbreak attacks.

### Strengths
1. This paper studies jailbreak attacks from a novel perspective like software engineering, to synthesize (all) jailbreak attacks and evaluate the jailbreak robustness of LLMs.

2. The experiment is comprehensive and the visual analysis is clear.

3. The discussion part is detailed.

### Weaknesses
1. Section 3.1, especially line 166-167, makes this reviewer confused. It seems that Section 3.2 has few connections with Section 3.1. To specific, the description in Section 3.1 does not significantly contribute to this reviewer's understanding of the connection from the motivation to the method of this paper. For example, this reviewer wants to know more details about the generic decorator TransformFxDecorator and why it covers the space of all string-to-string transformations and could represent any jailbreak attack on black-box LLMs.

2. Based on the first point, the reviewer is concerned that the author's claim of “representing all black box attacks” is an overclaim. As the author cited in Section 2, PAIR, and its following version TAP, employ a red-teaming assistant to jailbreak the target model. So the algorithm output is uncertain. The authors should explain the inclusive relationship between h4rm3l and other black-box jailbreak attacks.

3. According to this reviewer's understanding, the process of synthesizing jailbreak attacks briefly includes two sub-processes: selection, composition, and evaluation. Section 3.2 and 3,3 describe the details of selection and evaluation, respectively. However, how are the selected jailbreak methods combined in this paper?

### Questions
This reviewer's questions focus on the methods' details. See weakness 1-3. This reviewer wants to know more about the details of this method.

### Soundness
3

### Presentation
2

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
The paper proposes h4rm3l, a domain-specific language designed to describe and facilitate jailbreak attacks on language models. h4rm3l addresses the gap between the diversity of jailbreak attack techniques and the limited benchmarks currently available. It formally expresses jailbreak attacks as compositions of parameterized string transformation primitives, enabling it to capture a wide range of attack types and their combinations. Furthermore, h4rm3l incorporates a bandit-based approach to jailbreak attacks and synthesizes a dataset containing 2,656 successful novel attacks targeting six state-of-the-art (SOTA) open-source and proprietary LLMs. The results demonstrate that the synthesized attacks are diverse and significantly more successful than previously reported methods, achieving success rates exceeding 90% on these SOTA models.

### Strengths
h4rm3l offers a formalized framework for representing jailbreak attacks, addressing the need for a consistent, standardized approach in this area of research. By utilizing parameterized string transformation primitives, it enables the modeling of diverse and complex attack types, making it a versatile tool. Notably, h4rm3l has demonstrated impressive empirical success, achieving over 90% success rates in generating jailbreak attacks across several state-of-the-art language models, including GPT-4o, Claude-3, and Llama3. This showcases its robustness and effectiveness in exposing vulnerabilities in a wide range of LLM architectures, proving its scalability and relevance for both proprietary and open-source systems.

### Weaknesses
While the paper is impressive, it does not sufficiently address its limitations. Beyond the template-based jailbreak methods and synthesis, other forms of jailbreak techniques exist, such as fuzzing or mutation-based or other approaches ([1], [2], [3]). Given that the authors propose a language to express various attack strategies, it is important to clarify the scope of h4rm3l in this regard. The paper should discuss how many types of jailbreak methods the language can effectively cover and whether it faces any limitations in representing certain attacks. Furthermore, it would be beneficial if the authors included a more comprehensive discussion of related work in the background section, addressing whether h4rm3l can accommodate or has limitations in expressing these alternative attack types.

[1] https://www.usenix.org/conference/usenixsecurity24/presentation/yu-jiahao
[2] https://www.usenix.org/conference/usenixsecurity24/presentation/yu-zhiyuan
[3] https://www.usenix.org/conference/usenixsecurity24/presentation/liu-tong

### Questions
1. To what extent can h4rm3l cover alternative jailbreak techniques, such as fuzzing or mutation-based attacks, beyond template-based methods?
2. Could the paper further discuss how h4rm3l compares to other jailbreak methodologies and clarify whether it can fully accommodate these approaches or has constraints?

### Soundness
3

### Presentation
4

### Contribution
3

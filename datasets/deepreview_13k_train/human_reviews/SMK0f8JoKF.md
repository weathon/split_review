# Language Models Are Implicitly Continuous

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Language is typically modelled with discrete sequences. However, the most successful approaches to language modelling, namely neural networks, are continuous and smooth function approximators.
In this work, we show that Transformer-based language models implicitly learn to represent sentences as continuous-time functions defined over a continuous input space. 
This phenomenon occurs in most state-of-the-art Large Language Models (LLMs), including Llama2, Llama3, Phi3, Gemma, Gemma2, and Mistral, and suggests that LLMs reason about language in ways that fundamentally differ from humans.
Our work formally extends Transformers to capture the nuances of time and space continuity in both input and output space.
Our results challenge the traditional interpretation of how LLMs understand language, with several linguistic and engineering implications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors explore how Transformer-based language models, which traditionally operate on discrete token sequences, can implicitly represent language in a continuous manner. They introduce a novel continuous extension of Transformers, termed the Continuous Causal Transformer (CCT), allowing models to handle continuous inputs in both time and space. Through experiments on state-of-the-art models like Llama3 and Mistral, they demonstrate that these models exhibit continuity in their internal representations, causing different responses to variations in input duration and interpolation between tokens. The findings suggest that these models create implicit, continuous representations that differ fundamentally from human linguistic understanding.

### Strengths
The paper explores the intriguing hypothesis that language models, despite being trained on discrete sequences, learn to form inherently continuous representations of language. To investigate this, the authors propose a formalization of continuous Transformers, which "collapse" back to the discrete case when evaluated at discrete time steps. This formulation offers flexibility to probe the nature of model representations, such as by adjusting the "duration" of tokens in a sequence. The paper clearly articulates this formulation and its expressive power, laying a solid foundation for the subsequent experiments.

The experiments logically build on this framework and provide support for the hypothesis that models represent language in a continuous manner. For example, by modifying the duration of tokens in a sequence of repeated items, the model produces varied answers to simple counting tasks, indicating a sensitivity to continuous input features. In another set of experiments, interpolation between the representations of two tokens shows how the model continuously change its prediction according to the "weight" of each token in the interpolation.

Overall, the main contribution of the paper is providing a framework for thinking about LMs as continuous processes, which lends itself to simple probing experiments on the nature of LM representations.

### Weaknesses
I don't find any weakness in the theoretical formulation. I have some reservations regarding the *interpretations* of the findings and the lack of reference to previous work on the subject:

* First, I am not entirely clear on the details of the experiment in Section 4.1. Am I correct in understanding that this setup is no longer equivalent to a "regular," discrete Transformer, as the duration of different tokens is no longer uniform? Could the model, in principle, have learned a different behavior (i.e., the "human" interpretation of the sequence)? Specifically, is it correct that when using, for instance, a duration of 0.25 for each of the four occurrences of "apple," the attention dedicated to them would be identical to the attention given to a single occurrence of "apple" in a standard Transformer? If this is indeed the case, the result is unsurprising, as the representations fed into the model would be identical to those in the prompt, "In the sentence 'apple,' how many fruits are mentioned?". In that case, the manipulation in that experiment is just a different way to acknowledge the fact that LMs are fed continuous vectors and not discrete symbols.

* The interpolation experiments in Section 4.1 do provide evidence of the continuous nature of language model representations. However, these findings are not novel, and the paper lacks sufficient references to a substantial body of prior work. The continuous representation of distinct symbolic linguistic processes dates back to the creation of dense vectors via SVD of PMI matrices. Additionally, in interpretability research, there has been extensive work on the continuous representation of symbolic properties, such as linear concept erasure, which identifies specific manipulations in the latent space to isolate particular concepts.

### Questions
One possible use case of the theoretical framework proposed in the paper is probing which continuous space model best matches the one learned by the LM, i.e., we can come up with different continuations schemes and examine which best matches the observed one. Does that make sense? do you have any thoughts about that?

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
4

### Summary
This paper aims to demonstrate that transformer-based language models not only learns to process input sequences consisting of discrete tokens, but are also able to "reason" about the continuous interpolation of discrete tokens along the temporal and spatial dimensions. The paper first presents a continuous generalization of the classical transformer model to make it accept spatially and temporally interpolated continous inputs. It then shows via exemplar analyses that one can manipulate the "temporal duration" of input tokens to control model prediction on simple reasoning tasks; it also shows that the "spatial interpolation" of input tokens, formulated as their weighted averages, also elicit meaning outputs from the tested language models. The authors therefore claim that LLMs process natural language in a way that is fundamentally different from human speakers.

### Strengths
1. The continuous generalizations of key transformer modules such as multi-head self-attention seem novel and theoretically sound.

2. The presented examples of controlled input manipulation and the resulting model predictions in section 4 are interesting and intuitively make sense.

### Weaknesses
1. Despite the novelty of the main arguments and the proposed continuous generalization of transformers, the paper did not provide suffcient empirical evidence and quantitative evaluation to support them. In particular, the analyses in section 4 are based on only a couple of example input sequences, with a very special type of prompt template. It would make this section more convincing if the authors could curate and evaluate LLMs on a dataset of "temporally" or "spatially" interpolated input sentences, and define a more general evaluation metric to capture the variation of model prediction when manipulating the time durations or spatial weights of target tokens.


2. The claim that "LLMs reason about language (continuously)" seems also to be an overstatement given the input- and output-level simplicity of the evaluation tasks (e.g. counting the mentions of certain entity type in a short sentence). I'm curious to see whether the model could still produce fluent outputs on more complex text generation tasks (e.g. long-form QA) if we manipulate input tokens as suggested in section 3. If not, it would suggest that LLMs in fact do not assign meaningful representations for the spatio-temporally interpolated counterparts of input token embeddings.

### Questions
For the single-token time continuity test in section 4.1, what would happen if you use input prompts with different entity names from the same category? (e.g. In the sentence "apple banana pear orange", how many fruits are mentioned?)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper shows that Transformer language models (LM) implicitly learns continuous sentence representations in both space and time dimensions. The paper generalizes the standard discrete LM inputs to continuous cases, and demonstrate some interesting phenomena like stretching input sequence lengths can bias predictions accordingly (time continuity), and interpolating two inputs enables the model to generate meaningful outputs (space continuity). The paper argues that treating LM as continuous models deepens our understanding of its nature and promises performance improvement.

### Strengths
The paper provides a novel perspective of analyzing LMs, that is its representations are implicitly as continuous. This is an interesting and insightful observation that deserves follow-up analysis and further investigation.

### Weaknesses
Evidences supporting the claim that LMs are implicitly continuous are not sufficient and limited. Deeper analysis and more diverse experiments are desirable. The paper's exploration of temporal continuity, while interesting, lacks a rigorous examination of how the model behaves when presented with truly continuous input signals rather than stretched discrete sequences. The spatial continuity argument relies heavily on analogies to word vector algebra, and the examples provided do not fully leverage the unique capabilities of LMs. The implications of the continuity observations for controlling LM behavior and improving its quality are not well-established, and the proposed directions remain vague and lack concrete experimental validation.

### Questions
1. If the claim that LMs are temporally continuous, then what if we give them input sequences which are curves that fit the discrete token inputs? In other words, we can consider discrete token inputs as "samples" from continuous signals, so it's natural to ask what would the outputs look like if we input the LM with the original "continuous" signals.

2. Evidences provided by the paper to support the claim that LM is "spatially continuous" (Sec 4.4) are pretty much the same as the classical word vector algebra (e.g. "queen" - "woman" + "man" = "king"), and kind of expected. It might be more interesting to provide some more sophisticated examples that are unique to LM's capabilities, for example interpolating between two logic expressions that a LM can predict well, and observe whether the model is able to find novel logical relations.

3. While it is interesting to provide observations indicating that LMs are time and spatial continuous, what are the implications of this finding on controlling LM behavior and improving its quality? The paper only briefly mentioned some items in Sec 5, but they do not appear to be very concrete or convincing.

4. Beyond the examples that the paper provided, it would be more interesting and insightful to train a LM with inputs being compressed or stretched (like in the time duration cases), or just do inference on a wider variety of more difficult tasks (e.g. reasoning, coding, maths etc.), and compare model behavior differences.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper looks at transformer architecture (function) from a step function mixture viewpoint and proposes a continuous generalization of the transformer architecture by introducing token duration. From here, the paper investigates into two genres of properties of the transformer architecture (both quite linear) from the transformer architecture:
- time wise, the architecture is shown to be quite linear with time (through for example counting experiments)
- space wise, the architecture is shown to be able to perform linear interpolation on semantic space

The paper also shows some invariance/variance properties of currently used position embeddings.

### Strengths
The experiments that vary the duration is interesting and looks novel to me; besides, it follows directly from the established continuous extension of the transformer architecture. The paper shows that the counting or to some extent meaning retention has some correlation with the token duration through various experiments. 

It is nice to see semantic interpolation for LLMs, although this is a well known results for word embeddings.

### Weaknesses
While the time duration looks interesting and novel, I am not able to tell from the paper what are the experimental settings used to produced the results in the paper (I have put my exact questions in the question section). Thus unfortunately, I am not able to reproduce such experiments and I am not able to see any insights for cause and effects of this phenomenon.

shifting-invariant and scale-variant are well known effects and can be derived directly for models using ROPE embeddings and such properties hold similarly for a large range of models. Such contribution in the paper does not match ICLR acceptance standard, I think.

### Questions
What are the exact experimental settings to produce results in 4.1 and 4.2 please? More precisely:
- How are durations taken into account in the modification? Are these done through attention modification as shown in eq (4)?
- How are position embeddings handled in those experiments? When duration is longer/shorter, do authors also adjust position embeddings to reflect the duration change please?

### Soundness
2

### Presentation
2

### Contribution
2

# Modeling Real-Time Interactive Conversations as Timed Diarized Transcripts

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 5, 3

## Abstract
Chatbots built upon language models have exploded in popularity, but they have largely been limited to synchronous, turn-by-turn dialogues. In this paper we present a simple yet general method to simulate real-time interactive conversations using pretrained text-only language models, by modeling \textit{timed diarized transcripts} and decoding them with \textit{causal rejection sampling}. We demonstrate the promise of this method with two case studies: instant messenger dialogues and spoken conversations, which require generation at about 30 tok/s and 20 tok/s respectively to maintain real-time interactivity. These capabilities can be added into language models using relatively little data and run on commodity hardware.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper describes a method for applying a standard LLM to the task of generating dialogues incrementally, either turn-by-turn or word-by-word, by considering an output as a triple of (utterance time, speaker, message) and predicting on that basis. Experiments are given with turn-by-turn text-based instant messaging, and word-by-word text-based dialogue (starting with spoken dialogue, but processing with ASR to a text transcript and then experimenting on that). Experiments show that some plausible outputs can be generated, that generally bigger LLMs outperform smaller ones, and that the better models can receive good ratings from human evaluators.

### Strengths
The paper deals with interactive online generation of dialogue, in both message-by-message and word-by-word scenarios; this is a really important task from the point of view of building genuinely interactive conversational agents, and one that really hasn't seen much attention recently. The approach taken is quite intuitive to understand and is explained quite clearly. The evaluation shows that the approach can be effective, not only in generating coherent dialogue turns but including some important dialogue phenomena such as self-repair and turn-taking phrases (as shown by the examples in the appendix).

### Weaknesses
There is a fairly large amount of pre-LLM work on the details of incremental word-by-word dialogue modelling, including agents that can listen and generate on a word-by-word basis: the paper cites Skantze (2021)'s review of turn-taking treatment but would be stronger if it gave more comparison to work in that area.

The evaluation gives comparisons between LLMs on general metrics, but could be stronger if it looked at more details of coherence, turn-taking etc. It would be really nice if there was some discussion (quantitative or qualitative) of the linguistic phenomena that do/don't seem to be captured by this approach: the paper mentions coherence and consistency, but word-by-word and turn-by-turn modelling mean that other issues become important, e.g. realistic turn-taking patterns, interruption and overlap. The appendix transcripts show that some cases display good examples of some of these, some less so.

The evaluation uses data with a fairly low level of interactivity compared to many dialogue datasets. Instant messaging is an asynchronous, turn-by-turn medium; the spoken dialogues must be treated more incrementally, and are modelled word-by-word, but come from court transcripts in which the level of formality is high, and thus speaker changes, overlaps, interruptions etc are likely to be rare compared to more everyday, informal conversation. It would be helpful to know more about the average turn length, turn duration, number of speaker changes etc in this data compared to some of the more standard conversational datasets used in dialogue system development.

The model is one of generating a transcript as a whole, including all participants, whereas a practical conversational agent would have to react to other agents' contributions, online, and continue to adapt as their contributions come in (possibly interrupting, overlapping, leading to conversational directions that are not in the agent's interest, etc) - so some discussion of what would be involved in fitting this approach into those kind of constraints would be very helpful. 

Relatedly, the model's basic assumption that p(e|context) can be decomposed into p(t|context) x p(s|context,t) x [...] seems to mean that it's predicting an utterance event time, and then predicting the speaker of that utterance event. A more realistic agent might predict speaker (or know that it wants to speak) first, and then need to predict when to speak - would that fit with this approach?

### Questions
See weaknesses above

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
2

### Summary
The paper presents a method for simulating real-time interactive conversations by modeling diarized, timed transcripts, combined with causal rejection sampling. This method enables pre-trained, text-only language models to handle asynchronous and synchronous dialogues, as demonstrated with case studies involving instant messaging and spoken conversation simulations. The approach aims to maintain interactivity with minimal hardware requirements, while retaining a natural flow of dialogue.

### Strengths
1. Introduces a feasible approach for real-time interaction modeling using timed diarized transcripts and causal rejection sampling, which can be integrated into standard pre-trained models.
2. Demonstrates applicability with two distinct real-world cases: asynchronous instant messaging and real-time spoken conversations, adding diversity to potential model interactions.

### Weaknesses
1. There is little comparison with already existing work in this area (i.e. https://arxiv.org/abs/2405.19487) 
2. The model is trained on narrow datasets (instant messaging and court transcripts), raising doubts about its generalization to diverse, real-world conversational scenarios.
3. Reliance on ASR and TTS systems may introduce errors and disrupt natural flow in spoken dialogues. An end-to-end audio model could reduce these issues by handling speech inputs and outputs directly.

### Questions
1. What considerations were made regarding the potential for user fatigue in interactions involving high rejection rates in real-time conversations?
2. Have you considered building an end-to-end model? Integrating ASR and TTS into the LLM as well to achieve faster response times?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a method for simulating real-time interactive conversations using pretrained text-only language models, incorporating two key modifications. First, it employs timed diarized transcripts to represent each timestamped event, with each entry consisting of a timestamp, speaker ID, and message content. The model is tasked with predicting the probability of the next event based on event history, and sampling can proceed token by token, similar to standard causal language model text generation. During inference, a technique termed causal rejection sampling enables real-time interaction by discarding and resampling responses when interrupted by the user, thus adapting to dynamic input. To improve response speed during user interruptions, the authors also introduce two enhancements: (1) accounting for model generation latency and user reaction time and (2) applying a modified speculative decoding method to reuse partially generated responses before interruption.

The method is evaluated in two domains: instant messaging and spoken conversation. For instant messaging, the authors processed a 9-year message history between the first authors, resulting in 37 million characters in the diarized transcript format. For spoken conversations, they utilized a 1000-hour subset of U.S. Supreme Court oral arguments, totaling 33 million characters. This spoken data was converted into word-level transcripts with precise timing using an ASR engine. Experiments involved both open-source LLMs (Pythia, Gemma, LLaMA) ranging from 160M to 7B parameters, and state-of-the-art proprietary LLMs. Evaluation metrics included document-level perplexity, offline human evaluations ranking generated continuations, and online human evaluations involving direct interaction with the model. Key findings indicate that (1) the method meets real-time interactivity constraints on feasible hardware (e.g., a 40GB A100 GPU for a 7B LLaMA 2 model), and (2) larger, high-quality LLMs generally perform better in real-time interactive conversation modeling.

### Strengths
- Adapting text-only LLMs to model real-time interactive conversations is an important yet underexplored problem with the potential to unlock new applications without the need for costly retraining. The proposed method is straightforward but effective, demonstrated across a variety of LLMs from different model families and scales, and applicable to both fine-tuning and in-context learning.
- The paper includes both offline and online human evaluations in addition to automatic metrics, which are particularly valuable for assessing the performance of LLMs.

### Weaknesses
 - A critical aspect of real-time conversation is that the user can interrupt at any moment, requiring the model to discard its current response and handle the new input immediately. However, while the proposed method has the potential to address this, it is not thoroughly tested in the experiments. There is not even a qualitative example showing such behavior from the trained models.
- Using instant messaging dialogues to evaluate real-time interactions may not be ideal, as people’s response habits vary depending on availability, typing speed, and other factors. Modeling response timing directly may be less meaningful in this setting, and the turn-based nature of messaging lacks the fluidity and interruption dynamics of real-time conversations.
- The human evaluation lacks details, such as the number of conversations evaluated per method, the evaluation rubric, and consistency across ratings. It is unclear how the conversations are compared or if a consistent standard was applied, which is particularly important given the challenge of evaluating long texts.
- The control tokens introduce significant overhead in the spoken conversation domain without an optimized tokenizer that treats numbers from 0 to 999 as single tokens. Since existing models may not support such tokens, this limits the method’s practicality when used with standard tokenizers.

### Questions
Q1: Could you clarify what is meant by the "first 95%"? Is this based on chronological order? If so, wouldn’t this temporal split risk introducing shifts in topics or conversational styles over time, potentially affecting the robustness and validity of the evaluation?
> We use the first 95% of the messages as the train set, the next 2.5% as a validation set, and the last 2.5% as a test set.

Q2: In Figure 4, timing is evaluated based on the delays between successive messages. Could you clarify why only delays are measured rather than both delays and any potential early responses? Additionally, how is the alignment between generated and ground-truth messages determined? If the generated messages differ significantly in content from the ground-truth, what is the meaning or value of comparing the timing between two sets of messages that may not correspond closely in their content?

Q3: Why were different evaluation metrics used for human assessments in the instant messaging and spoken conversation settings? Could you explain the reasoning behind this choice and how it aligns with the specific goals of each domain?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a novel approach for achieving real-time response in dialogue systems by modeling timed, diarized transcripts and decoding through causal rejection sampling. The model is tested on both instant messenger dialogues and spoken conversations, with results demonstrating its ability to sustain real-time interactivity.

### Strengths
The proposed dialogue system supports multi-speaker, simultaneous conversations, marking a significant advancement over traditional turn-by-turn dialogue models. Additionally, the method’s design allows it to be easily integrated into various models, demonstrating its versatility and broad applicability.

### Weaknesses
1. Additional Evaluation Metrics to Consider
- While the model demonstrates high generation bandwidth, how does your approach ensure the model engages at the right time rather than speaking continuously? In other words, how does your method balance high generation rates with appropriate turn-taking? Specifically, what mechanisms prevent the model from generating responses that overlap significantly with user turns, and how is this behavior quantified beyond the timing visualizations provided? A more detailed analysis of turn-taking behavior, including metrics like turn overlap ratio and the frequency of appropriate response timing, would be beneficial.
- An ablation study comparing models without rejection sampling and those fine-tuned for next-turn speaker and response prediction could help validate the model design. It is unclear how much of the real-time performance is due to the causal rejection sampling versus the underlying model's ability to predict appropriate turn-taking. An ablation that removes rejection sampling and compares it to a model trained with explicit next-turn prediction would isolate the impact of each component.
2. Positioning and Contribution

This paper proposes a system design for real-time conversation. However, its novelty from a learning and evaluation perspective isn’t fully highlighted. The paper needs to more clearly articulate how its approach differs from existing methods for modeling timed event sequences, particularly in the context of interactive systems. It would be beneficial to discuss how the proposed method's end-to-end approach compares to systems that use a combination of specialized models or hand-engineered heuristics, and to clarify the specific advantages of the proposed method over these alternatives.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2

# Large language models as windows on the mental structure of psychopathology

- Decision: Reject
- Scores: 1, 6, 5, 5

## Abstract
How people represent the world determines how they act on it, as these internal representations bias what information is retrieved from memory, the inferences that are made and which actions are preferred. The structure of these representations are built through experience by extracting relevant information from the environment. Recent research has demonstrated that representational structure can also respond to the internal motives of agents, such as their aversion to uncertainty, which impacts their behavior. This opens the possibility to directly target internal structures to cause behavioral change in psychopathologies, one of the tenets of cognitive-behavioral therapy. For this purpose, it is crucial to understand how internal structures differ across psychopatologies. In this work, we show that Large Language Models (LLMs) could be viable tool to infer structural differences linked to distinct psychopathologies. We first demonstrate that we can reliably prompt LLMs to generate (verbal) behavior that can be detected as psychopathological by standard clinical assessment questionnaires. Next, we show that such prompting can capture correlational structure between the scores of diagnostic questionnaires observed in human data. We then analyze the lexical output patterns of LLMs  (a proxy of their internal representations) induced with distinct psychopathologies. This analysis allows us to generate several empirical hypotheses on the link between mental representation and psychopathologies. Finally, we illustrate the usefulness of our approach in a case study involving data from Schizophrenic patients. Specifically, we show that these patients and LLMs prompted to exhibit behavior related to schizophrenia generate qualitatively similar semantic structures. We suggest that our novel computational framework could expand our understanding of psychopathologies by creating novel research hypotheses, which might eventually lead to novel diagnostic tools.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes to examine LLM representation as a parallel with certain psychopathologies, such as apathy, depression, or anxiety. 
LLMs are first prompted in various manners to exhibit such conditions, and then an assessment of their internal structure is done via prompting for word associations and measuring distances with Glove embeddings. Then these metrics are compared to human subject data collected in previous study to see how much of it is explained by the LLM performance.

### Strengths
- I think that it's timely project to examine the correlations between human and LLM behavior, and the idea to correlate that carefully against existing data is interesting.

### Weaknesses
Despite the timeliness of the work, I have major concerns about it in its current state.

* **Methodology** - Most importantly, I doubt the methodology, and hence doubt also the results obtained from it.

First, there seem to be some implicit parallels drawn in this work between LLMs and human subjects, but this is not made explicit. Instead the paper refers to the "structure" of LLMs, which is unclear to me. There's a point to be discussed that the inner representation of the LLMs are its weights, in which case, it's the same LLM when different prompts are made, which I think contradicts the paper approach that the LLM personifies different subjects with a different prompt. In contrast, it's possible to claim that the representation of the LLM is composed of its weights + the activations induced from the prompt, which would better fit the paper claim, but none of this non-trivial point is discussed or argued by the paper.

Second, I find the initial experiments (Figure 2, and the evaluation of co-morbidities) highly questionable, and hence as the paper states this is "an important result that forms the basis for the following analyses", I consequently doubt the following results. I doubt figure 2 because of other possible explanation beyond an actual "underlying psychopathology" in LLMs (Line 285), e.g., since all of these exams are available online, it's very probable that they appeared in the LLM pretraining corpus (contamination), which actually I think aligns with the paper's finding that LLama, Mistral show high scores "even when prompted with no pathology" (Line 260). The correlation between different conditions is an interesting way to alleviate these concerns, but here too I disagree with the chosen methodology, the paper compares the different models relatively to one another and chooses the one which better explains human data: "Dolphin displays
the highest correlation (0.59..." (Line 301). I don't think that these measures should be taken in a relative manner. Instead, I think that models should clear some absolute bar to be considered as correlated with humans. For example, how do human subject correlate on this scale? Is 0.59 significant? Also, I don't know if RSA is a common way to compute such similarities, the paper doesn't cite a source for this comparison.

Finally, I disagree with the paper's claim that the experiments conducted in Section 4.1 are relevant proxies for "representational structure". Equations (1) and (2) aren't motivated in literature or in concrete evidence that they reflect inner representation (a terms which wasn't explicitly defined, as I mentioned above). Even if justified, I find the use of Glove embeddings highly questionable -- from what I understand it is taken as a sort of "gold" representation for semantic diversity, which isn't justified, explained, or evaluated. Instead, I would work on justifying why equations (1), (2) are correlated with some explicit inner representation, and then evaluate it manually for at least a subset to understand how well glove approximates this score.

* **What are the actual takeaways?** -  
I struggle with understanding what would be the takeaway of the paper? How would it benefit future research? The paper says in the conclusion that "We suggest that our method can help generating novel hypothesis regarding the between link mental structure and psychopathology, in a cost effective and scalable way" (Line 482). How? Is it possible to flesh this out more?

* **Appropriateness for ICLR** - Related to the previous question, I wonder who would be the appropriate audience for this paper. If the conclusions benefit psychologists, then perhaps it's a better fit at that kind of venue? Relatedly, there are many claims made in the paper about psychology (e.g., in Section 3.1), which I'm not qualified to review, since I don't have any expertise in this area.

### Questions
- What's the license of the data used in this work? Did the subjects give their consent for this kind of use?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed a way to leverage LLMs to generate dialogues, which can be used to evaluate whether it shows psychopath or other symptoms. The authors also foresee that this method can be used in practical fields like Cognitive Behavioral Therapy. The authors conducted thorough analysis with different open models, and conducted statistical significance measurement.

### Strengths
- The authors performed thorough design and analysis on the performance of the framework with different open models
- The authors conducted analysis on statistical significance

### Weaknesses
From an outside perspective, one could argue that the results show the possibility of priming models to mimic (and I am using this term in a strictly technical sense) the language behaviour observed in human patients with mental disorders. This can either display how strongly the field of psychopathology is bound to language or the limitation of questionnaires to fully capture it. To be fair, the authors never claim anything they did not substantiate with results, but my general concern is about how relevant this is regarding the understanding of psychopathology. Their approach certainly helps formulate new hypotheses to explore the language dynamics correlating with mental disorders and may help differentiate the latter from other human behaviours. However, the results only show post hoc correlations of answers but not evidence that these to-be-generated hypotheses can be meaningful.

More precisely, the authors analysed many representations of the LLM output (words that make up the answers) but not the output representation (the hidden states generated by the underlying transformer that shape the probability distribution from which tokens are sampled). The correlations displayed are certainly interesting as they seem to align the response behaviours of models and humans, but there is no justification for this correlation to be meaningful.

If, for example, during pre-training, an LLM encountered enough material about clinical tests and the answers correlating with the presence of a mental disorder, it may just display these correlations in its response behaviour. If the authors could instead use their approach to design a concrete hypothesis (which is the intended contribution of their article) and verify it using human data (which may not necessarily require the collection of new data), I would be more convinced that the displayed connections are meaningful. In essence, I think it is necessary to test how human response behaviour in a novel setup aligns with the LLM's response behaviour and not vice versa, as we cannot distinguish the degree to which models only imitate what they learned during training.

I am unsure whether the authors used the foundation models or the instruction-tuned versions for their experiments. This information needs to be added for clarity as instruction-tuned versions have been trained to adhere to (specially formatted) system prompts that can influence the impact of instructions on the generation behaviour.
Also, as the experiments require no fine-tuning, adding more modern iterations to the model pool (such as GPT-4/o/o-mini or Llama-3, which was published several months ago) seems promising. In this context, it would also be interesting to investigate how the scores scale with parameter size - has this been considered? Since most LLMs nowadays are based on the Transformer architecture and performance mainly depends on parameter size and data quantity/quality, scaling laws for any emerging capability are desirable.

The authors generate answers using three different temperature values, but other generation methods, such as beam search and contrastive search, are not explored.

Figure 2 shows the pathology scores for primed and unprimed models and the diagnostic reference threshold. Why are the "No Pathology" bars different across the three prompting techniques? For example, for Social Anxiety, we see decreasing scores for Mistral -> Dolphin -> Llama when using Naive prompts but increasing scores for the React prompts. From my understanding, the "No Pathology" results are not influenced by any prompt template, so why do we observe these contradicting trends when averaging the performances over 100 simulations? Likewise, the "No Pathology" scores crossing the diagnostic reference threshold seem to depend on the prompting technique.

In general, why do the "No Pathology" scores vary so much across the different prompting techniques when averaging them over 100 simulations and using a low temperature of 0.3? Can the authors explain this?

The heatmaps in Figs. 8-12 show that there exist significant "side-effects" when inducing a specific mental disorder pattern using any of the prompt templates. This has been acknowledged in the text and linked to data observed in humans (testing positive w.r.t. more than one mental disorder questionnaire), but I feel that it also limits the scope of the approach. The red fields make it easy to spot whenever a perfect score of 1.0 is achieved, but they also slightly divert the attention from the other fields that show a value of 1.0. For example, in Fig. 8, several off-diagonal tiles also show a value of 1.0, and many values change drastically across the different prompting templates. Which of these values are meaningful? Does it make sense to evaluate the minimum/maximum?

Also, more information is required: the authors cite some works in the paragraph starting in line 280, but it is unclear which of the observed patterns in the normalised Lickert scores are mirrored by human behaviour. A more detailed analysis is needed to convince readers that these patterns are meaningful (it would likewise be appropriate to move at least one of the figures to the article's main body).

The cosine similarity between two vectors is a common metric to compare how aligned they are (helping to compare vector representations of semantic concepts). However, the simplex volume needs more (mathematical) motivation and an explanation for why this expression is well-defined.

The results displayed in Figure 5 seem inconclusive. As can be seen by the (red) outliers in both human and LLM "Patient" data, determining the mean seems less adequate than, for example, the median (also, the standard error bars are difficult to detect, even when zooming in - increasing the thickness of the bars or the transparency of the dots may improve the plots). Instead of this quantitative analysis, I think it would be more attractive to qualitatively explore what may have caused the outliers to be significantly higher in human and LLM data. This could lead to formulating a concrete hypothesis (based on LLM data) for further testing and verification (with human data).

Overall, the article is good and a solid basis for future work, but I think the experimental results, albeit interesting, are too superficial. More evidence is needed to show why this approach is meaningful. However, I am open to being convinced otherwise and to change my rating.


Minor:

What is “PT-prompting” in Figure 1? Does it refer to “psychological traits”-prompting? 

The quality of the figures needs to be improved, especially for Fig.s 8-12.

Grammar and spelling mistakes need to be corrected, for example:

Line 020/021: “could be viable tool to” -> “could be viable tools to”

Line 051/052: “one of the basis of” -> “one of the bases of”

Line 313/314: “To evaluate representational” -> “To evaluate the representational”

Line 394/395: “sources words” -> “source words”

Line 396/397: “generate words embeddings” -> “generate word embeddings”

Line 430: “extract using” -> “extracted using”

Line 482/483: “novel hypothesis” -> “novel hypotheses”

Line 502: “green red” -> “red”

Line 510/511: “future as a ease-to-use of psychological tasks” -> best to rephrase that entire sentence

Line 518/519: “(Nour et al., 2023), measures.” -> “(Nour et al., 2023).”


Denoting the cosine similarity measure with “cos” is confusing.

Kappa and Delta need to be switched in lines 369 and 370.

In Figure 3, the RSA score heatmaps are at the top/middle/bottom (not left/middle/right). Also, the word “between” in the parentheses part needs to be removed.

### Questions
- Can you do more literature reviews on top conferences for similar approaches in psychology applications?

### Soundness
3

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
4

### Summary
The authors propose Large Language models (LLMs) as windows into the (human) mental structure of psychopathology. They prime models using instructions and descriptions of various mental disorders such as depression, schizophrenia, apathy, and others, before making them generate answers to the corresponding clinical questionnaires. They show that most tested models’ answers score high on the respective tests and above the diagnostic reference threshold. They then measure the impact of these primes on a word association task and show correlations with empirical results observed in humans. Finally, they finish with a case study comparing model outputs with the outputs of patients diagnosed with schizophrenia, again based on word comparisons.

### Strengths
The topic is very interesting. The experiments allow one to explore to what degree mental disorders can be tied to language and, therefore, be instilled and detected in LLMs as measured by the corresponding clinical questionnaires.

The article is well-written (apart from the grammar and spelling mistakes), well-structured and rich with empirical data and intuitive graphics. The overall presentation of results is very good.

The results show interesting correlations between the LLM output behaviour and what is expected to be observed in human patients diagnosed with the respective mental disorder. The general direction of research promises to reveal more interesting insights about how language is connected to the diagnosis and presence of mental disorders, which are separate points a priori.

The authors compare several models across 100 runs which broadens the experimental data and increase the representativeness of their results

The authors take care to delineate what their results do and do not show or implicate, which is especially important when dealing with sensitive topics like mental disorders and their diagnosis.

### Weaknesses
 - The abstract and introduction of the paper emphasize the importance of representations in understanding the inner workings of the mind. However, representations don’t seem to play any significant role in the experimental setup and analysis of the paper!  The prompted outputs seem to be used instead. A more direct approach comparing patient neural activation patterns with LLM embeddings may be needed to strengthen the claims.
    
- Line 25-26 talks about how lexical output patterns of LLMs are a proxy of their internal representations. However, this is very erroneous claim and much research has shown that models’ output as a function of their decoding strategy is not reflective of their internal representations.
    
- There seems to be a fundamental circularity in the experimental setup where we prompt models to generate psychopathic language and then we analyse the manipulated output to analyse the link between mental representation and psychopathology. But we specifically prompted models to behave this way and have these signatures that we look for later. It would be much more useful if we could use some kind of representational tuning of models with psychopathological representations and then analyse their output.
    
- There also need to be more models included to further strengthen claims (but this issue can only be addressed once the fundamental concerns highlighted before are fixed).

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the potential of LLMs as tools for investigating the mental structure of psychopathology. The authors demonstrate that LLMs can be prompted to generate text responses that score highly on standard psychopathology questionnaires. They then analyse the semantic structure of the generated text using word embeddings and find that different psychopathologies are associated with distinct semantic structures. The authors argue that this approach could lead to the development of new hypotheses about the relationship between mental structure and psychopathology.

### Strengths
- LLMs are becoming a part of our society and it is interesting to see work which attempts to elicit their use for benefit of society.
    
- Some findings consistent with empirical observations- the results for depression and anxiety are consistent with previous empirical findings, demonstrating the potential of LLMs to simulate certain aspects of psychopathology.

### Weaknesses
- The abstract and introduction of the paper emphasize the importance of representations in understanding the inner workings of the mind. However, representations don’t seem to play any significant role in the experimental setup and analysis of the paper!  The prompted outputs seem to be used instead. A more direct approach comparing patient neural activation patterns with LLM embeddings may be needed to strengthen the claims.
    
- Line 25-26 talks about how lexical output patterns of LLMs are a proxy of their internal representations. However, this is very erroneous claim and much research (Turpin et al 2023 etc) has shown that models’ output as a function of their decoding strategy is not reflective of their internal representations.
    
- There seems to be a fundamental circularity in the experimental setup where we prompt models to generate psychopathic language and then we analyse the manipulated output to analyse the link between mental representation and psychopathology. But we specifically prompted models to behave this way and have these signatures that we look for later. It would be much more useful if we could use some kind of representational tuning of models with psychopathological representations and then analyse their output.
    
- There also need to be more models included to further strengthen claims (but this issue can only be addressed once the fundamental concerns highlighted before are fixed).

### Questions
- The paper's experimental setup needs to be improved in light of suggested weaknesses

### Soundness
1

### Presentation
2

### Contribution
2

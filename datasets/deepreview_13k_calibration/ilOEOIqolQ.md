# AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Creativity has long been considered one of the most difficult aspect of human intelligence for AI to mimic. However, the rise of Large Language Models (LLMs), like ChatGPT, has raised questions about whether AI can match or even surpass human creativity. We present \metricname as the first step to quantify the linguistic creativity of a text by reconstructing it from existing text snippets on the web. \metricname is motivated by the hypothesis that the seemingly remarkable creativity of LLMs may be attributable in large part to the creativity of human-written texts on the web. To compute \metricname efficiently, we introduce \methodname, a novel dynamic programming algorithm that can search verbatim and near-verbatim matches of text snippets from a given document against the web. 
Experiments reveal that the \metricname of professional human authors is on average 66.2\% higher than that of LLMs, and that alignment reduces the \metricname of LLMs by an average of 30.1\%. In addition, we find that distinguished authors like Hemingway exhibit measurably higher \metricname compared to other human writers. Finally, we demonstrate that \metricname can be used as a surprisingly effective criterion for zero-shot machine text detection, surpassing the strongest existing zero-shot system, DetectGPT, by a significant margin of 30.2\%, and even outperforming the strongest supervised system, GhostBuster, in five out of six domains.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper discusses work on measuring the creativity of a language model’s generated content using a large compilation of web texts as reference corpus called Creativity Index. This metric quantifies how much the machine-generated text is remixed and matched from the reference corpus through an n-gram based analysis (re: L uniqueness, # of words outside n-grams normalized by words in text). This is then packaged into a DP-based search mechanism called DJ Search that efficiently attributes pieces of texts from the reference corpus. The paper has a number of well-discussed, well-visualized interesting results. This includes humans showing a consistent higher level of creativity compared to LLMs (52% higher than LLMs in novel writing, 31.1% higher in poetry composition, 115.3% higher in speech drafting). Supporting ablation experiments were also done by the authors on quantifying how much RLHF hurts creativity (30+% reduction), measuring creativity outside of the scope of the reference corpus, variance across humans’ level of creativity, and comparison to existing machine generated text detectors.

Overall I think this is a good paper for ICLR and has the level of completeness and technical rigor required for the conference.

### Strengths
The paper presents a good empirical investigation on the creativity (and and lack of) of large language models compared to creative inputs from humans. The proposed Creative Index is simple and easy to understand. The paper is readable, contains quality visualizations to complement experiment results, and has the level of completeness in terms of depth of experiments, discussion coverage, and insights. I also like and agree with the author/s’s analogy regarding how LLMs can be similar to DJ remixing information from different sources rather than a novelty-driven agent like real humans. Overall, the paper is a good addition to the conference.

### Weaknesses
I don’t have serious concerns from the paper, but a number of points can be considered to improve the overall quality of the work:

1. The first thing that readers will think of the proposed DJ Search is that searching for any form of patterns from an extremely large corpus such as RedPajama would be time inefficient (esp with size of the data). Even if the author/s say this is efficient, it should be emphasized in the main body of the paper itself including details of time complexity as I feel this part is not that stark / outright upon reading the paper. It might also be a nice-to-have to provide visualizations on how much time it would take for the algorithm to complete processing a sample dataset compared to other methods of searching in a visualized manner. The paper has some great visualizations so this part would be minimum effort.

2. Evaluating LLM’s quantified creativity is not new, therefore readers would expect some comparison between what is being proposed (Creativity Index) and what other creativity metrics are in literature. For example, does Creativity Index observe or correlate with some of the results from other tests such as Torrance Test of Creative Writing (TTCW, CHI2024) (https://arxiv.org/pdf/2309.14556)?  The authors can use the exact same test set with results from human annotations from this work and run them through the Creativity Index formula to analyze the results and identify which of the 14 aspects correlate together.

3. The vanilla version of WMD is old can faster variations have been proposed through the years including relaxed version (https://github.com/src-d/wmd-relax) and supervised version (https://papers.nips.cc/paper_files/paper/2016/hash/10c66082c124f8afe3df4886f5e516e0-Abstract.html). I suggest the authors explore these variations and document improvements to the paper.

### Questions
1. Can WMD be switched with simple Euclidean/Sinkhorn-based distance measures? What's the author/s' thoughts on this? Are there are any possible downgrades?
2. Is RedPajama the largest webcrawled data to use as reference? How about RefineWeb (https://arxiv.org/abs/2306.01116)?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The author presents Creativity Index that quantifies the linguistic creativity of text by reconstructing it from n-gram text segments from web sources.  The proposed indexing algorithm combines strict verbatim matching on text snippets and near-verbatim semantic matching on word embeddings. They have conducted comprehensive experiments using the proposed index to evaluate creativity between various human groups and both open-source and proprietary LLMs. 
The findings indicate that the current generative model reduces the ability to produce original and unique content, both verbatim and semantically, from human writing. An intriguing findings by the author is that preference alignment could significantly harm the model's creativity, decreasing it by 30% compared to the pre-trained model.
Overall, it is a well-organized and comprehensive research on the quantified assessment of model creativity.

### Strengths
- Well-crafted paper that clearly demonstrates the metric algorithm, experimental settings, and conclusions.  
- The motivation is well described at the beginning of this paper. The author managed to implement an effective method that is greatly aligned with the intention.
- The author conducted a multifaceted and multiangled extension of discussions, directly comparing LM and humans, exploring various matching algorithms, assessing RLHF on creativity, and potential usage on AI-generated text detection.

### Weaknesses
The metric method proposed in this article does not adequately support some of the findings presented. The main issues are as follows:
- Timeliness of Data: The majority of the text provided by RedPajama originates from internet sources dated between 2014 and 2023, with no precise creation dates included in the data. Many works by authors from past decades lack a sufficiently reliable text history to effectively apply the Creativity Index for analysis. Thus, it cannot be concluded that distinguished authors necessarily possess high levels of creativity.
- Depth of Matching Method Exploration: The article’s proposed method, which combines text and semantic matching, lacks an analysis of how each method contributes to the effectiveness of the metrics. Specifically, the paper does not provide a clear justification for the weighting or combination of these two matching approaches. It is unclear if one method dominates the other, or if their contributions are balanced. Furthermore, the semantic matching relies on word embeddings, which are themselves trained on large text corpora and may introduce biases or circularity in the analysis. The paper should explore the sensitivity of the results to different embedding models and similarity metrics.
- Lack of Baseline Metric Comparison and Analysis

The author mentioned the proposed DJ search using the two pointers to achieve linear search complexity. An analysis on searching common segments in the database would inform readers. The paper should include a more detailed analysis of the computational cost of the DJ search, especially in relation to the size of the reference corpus. It is not clear how the search time scales with the corpus size, and whether the linear complexity holds in practice for very large datasets.

### Questions
Please see the weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present two methods for analyzing text creativity:

DJ Search - A clever algorithm for finding the longest novel n-grams in a text by checking against a reference corpus

This paper is likely to have significant practical impact. Unlike many ML papers that require a cluster of A100s just to run inference, this could actually be deployed in real-world applications. The algorithmic approach means it can run on modest hardware and scale linearly with input size.

Plus, it's refreshing to see someone tackle the creativity measurement problem from first principles rather than just throwing more parameters at it. The information retrieval perspective brings some much-needed rigor to a field that's been getting a bit hand-wavy lately.

Accept. This paper makes a solid contribution to the field with practical, implementable algorithms. While there are some limitations, the core ideas are sound and the engineering considerations are thoroughly addressed. It's the kind of paper that will actually be useful to practitioners, not just citation fodder.

This is what good systems papers should look like - solid theoretical foundations, practical implementation details, and clear engineering considerations. Accept with enthusiasm, and looking forward to the GitHub repo (you are open-sourcing this, right?).

### Strengths
The paper's main contribution isn't just another transformer architecture trained on twice as much data - it's a genuinely novel algorithmic approach to measuring text creativity. The DJ Search algorithm is particularly elegant, reducing what could be an O(n²) operation to O(n) through a smart two-pointer approach. As someone who appreciates algorithmic elegance, this sparks joy.

The implementation details in Appendix A are great - they actually thought through the real-world engineering challenges instead of handwaving them away with "we leave this as an implementation detail." The optimization of Word Mover's Distance computation is particularly well done, showing they really care about making this practical.

They've included all the nitty-gritty details about corpus deduplication, handling edge cases, and optimizing the search process. This isn't just academic fluff - it's the kind of paper that an engineer could actually implement from.

The authors clearly understand the scale challenges of working with massive reference corpora. The BM25 pre-filtering approach for WMD is a smart compromise between accuracy and computational efficiency.

### Weaknesses
Classic ML paper moment - everything's tested on English only. Would love to see how this performs on languages with different n-gram distributions or morphological complexity.

The paper waves away the choice of α=0.9 and β=0.3 thresholds for corpus deduplication with a "in practice, we set..." Hand-waving intensifies. Some ablation studies would've been nice here.

The method's effectiveness is heavily dependent on the quality and coverage of the reference corpus. While they address this somewhat with the deduplication approach, there could be more discussion of how to maintain and update these corpora over time.

### Questions
Where is the github repo with code to make it easy to run this?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper tries to create a statistical metric to quantify creativity called CREATIVITY INDEX. The premise is fairly simple. They try to quantify creativity by checking what proportion of words are novel i.e those words are not part of ngrams that verbatim occur in pre-training data or is an approximate semantic match. They test a whole bunch of LMs both base as well as RLHF versions and experiment with various settings (nucleus sampling p, prompt format , model size). They also test on 3 type of writing tasks (novel, poetry, speech). The findings reveal that LLMs generated text have more verbatim matches from pre-training compared to human writing and hence they have lower CREATIVITY INDEX. The paper also show that CREATIVITY INDEX also adds as tool to detect machine generated text and outperforms DetectGPT and popular supervised baselines

### Strengths
The paper has many detailed experiments which I very much appreciate. Lots of graphs and figures to show different settings. The idea is very intuitive and from an engineering standpoint its of-course a very valuable contribution. Being able to trace text from pre-training is an excellent opportunity for the future of work and creative labor especially at a time when LLMs impact the livelihoods of professional writers. The structure and organization of the paper is also great.

### Weaknesses
There is so much to like about the paper. But there are obviously many limitations which makes me hesitant to give this paper a positive rating. I will try to be constructive here

1) From an experimental standpoint I think its important to fix top p to a higher value and vary temperature. Fig 4b plots CREATIVITY INDEX with respect to top p but we all know that when p = 0 the text is of course going to be repetitive. It does show that CREATIVITY INDEX increases with higher p. So this effect requires more rigorous testing where you fix the p and vary temperature

2) This is more technical term. But I do not think this paper is measuring Creativity. Authors mention "This metric is grounded in the notion of originality from creative thinking in psychology literature, which is defined as the statistical rarity of a response or an idea (Torrance, 1966; Crossley et al., 2016)." But Torrance Test has 4 broader components and just being Original is not enough for Creativity. This is my biggest complaint with the paper because the way it quantifies Creativity it would be super easy to game this metric by generating gibberish incoherent stuff that is not there in the pre-training. By authors' definition that is original wrt to Reference Corpus but is it Creative? I mean this as one of the biggest limitations of the paper. I do not think that novelty of ngram alone qualifies something to be more creative than the rest. So I request authors to update the paper and discuss these details. I think your metric quantifies Originality wrt Pre-training but that does not quantify creativity

3) One very big concern I had with this metric is how this can cause a lot of implicit bias towards writing that is simple yet evocative. I want to demonstrate some examples. I carefully checked that these texts occur in writings from other people (outside of the duplicate removal strategy which u applied)

   - **i) The context sentence**: "In the kitchen, she found herself reaching for the cabinet where her mother always kept the coffee, only to stop short"
     
     - **Expert Writer Written Continuation**: "This time, though, she was alone. Her mother would never come back."
     - **AI Written Continuation**: "The realization that she was alone here, truly alone, settled over her like a heavy blanket."
     
     Now obviously in context the AI written continuation contains a very cliched metaphor and is absolutely not original or creative in terms of writing. However, the human-written sentence has a richer subtext about the death of someone's mother which is expressed through simplicity and economical prose without using any flourish. Now I went to https://huggingface.co/spaces/liujch1998/infini-gram and copy-pasted the Human Written Continuation and found 6 occurrences of "This time, though, she was alone." and 94 occurrences of "mother would never come back." This means by your metric the expert-written continuation is less creative which I find untrue and somewhat problematic.

   - **ii) Coming to poetry**. Richie Hoffmann, one of the best contemporary poets, wrote a beautiful poem in *The New Yorker* titled "The French Novel" (https://www.newyorker.com/magazine/2019/04/08/french-novel). I mention the quatrain:

     > "[You were my second lover].  
     > You had dark eyes and hair,  
     > like a painting of a man  
     > We lay on our stomachs reading books in your bed."

     This was published in 2019. Now I searched Infinigram and found a poetry published in 2017 had one same sentence verbatim (https://cosmicrubble.com/2017/03/11/false-dawn/):

     > "[You were my second lover] ever in life,  
     > but I often wish you were my first"

     Now "dark eyes and hair" occurs 248 times in Infinigram; "like a painting of a man" occurs 24 times. "lay on our stomachs" occurs 604 times and "reading books in your bed" occurs 24 times. So based on your CREATIVITY INDEX you are saying the first quatrain is not Creative but they are originally written by an ex-Stanford Stegner Fellow.

   - **iii) Annie Ernaux** (Nobel Prize winner in Literature 2022) is popularly known for "Flat Writing." See this link https://www.nobelprize.org/prizes/literature/2022/ernaux/prose/

     Take the first excerpt from *Shame*: "One evening ‒ it was our last day ‒ in Tours, we had dinner in a brightly-lit restaurant where the walls were lined with mirrors, frequented by a sophisticated clientele. My father and I were seated at the end of a long table [....]"

     Infinigram Counts:
     - "it was our last day" → 8877
     - "dinner in a brightly-lit restaurant" → 1
     - "walls were lined with mirrors" → 147
     - "frequented by a sophisticated clientele" → 4
     - "My father and I were seated" → 15
     - "at the end of a long table" → 1826

     You need to be super careful with these sorts of claims in your paper. Because I think even though your intention is good, your metric accuses original writers or writers who aren't necessarily producing ngrams not in the reference corpus as not CREATIVE. There is a whole spectrum of writing. Verbatim matching text from pretraining does not reduce creativity; it’s more about juxtaposition of thoughts, how novel it is given the context/situation.

4) What impact does RLHF have on model creativity? This has already been studied by several papers so I don't see as any surprising thing.

5) How to measure creativity in LLMs trained on data outside of the reference corpus? Here again I appreciate that you found the similar models as GPT-4 cut off date like Gemma and Llama but I don't think you can use model-generated reference corpus. Especially there is evidence from ScaleAI that is used by Meta for RLHF data that workers themselves use ChatGPT / GPT4 https://www.wsj.com/tech/ai/alexandr-wang-scale-ai-d7c6efd7

6) This is a hasty and not well thought out claim "Our main finding is that classic literature exhibits a higher creativity level than the other two categories." What do you exactly mean by this? Books published in 2023 from the BookMIA (Shi et al., 2024) are a limited resource. In good faith, I cannot agree that books published now are less creative than Hemingway. That's like saying Murakami, Zadie Smith, Sally Rooney are less creative than Ernest Hemingway and William Faulkner. If you read literature, you know this is obviously not true.

### Questions
Have you considered doing some human eval on Creativity Ratings and measuring correlation with Creativity Index ?

### Soundness
2

### Presentation
4

### Contribution
2

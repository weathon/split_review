# EA2N: Evidence-based AMR Attention Network for Fake News Detection

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Proliferation of fake news has become a critical issue in today's information-driven society. Our study includes external knowledge from Wikidata and deviates from the reliance on social information to detect fake news, that many  state-of-the-art (SOTA) fact-checking models adopt. This paper introduces EA$^2$N, an Evidence-based AMR Attention Network for Fake News Detection. EA$^2$N leverages Abstract Meaning Representation (AMR) and incorporates knowledge from Wikidata using proposed evidence linking algorithm, pushing the boundaries of fake news detection. The proposed framework encompasses a combination of novel language encoder and graph encoder to detect the fake news. While the language encoder effectively combines transformer encoded textual features with affective lexical features, the graph encoder encodes AMR with evidence through external knowledge, referred as WikiAMR graph. A path-aware graph learning module is designed to capture crucial semantic relationships among entities over evidences. Extensive experiments supports our model's superior performance, surpassing SOTA methodologies. This research not only advances the field of Fake News Detection but also showcases the potential of AMR and external knowledge for robust NLP applications, promising a more trustworthy information landscape.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the detection of fake news on social media through the integration of external knowledge and evidence. The authors argue that existing related papers encounter three primary challenges: (1) the difficulty of capturing long-term and intricate semantic relationships, (2) unreliability and time-consuming knowledge acquisition processes, and (3) reliance on potentially unreliable information sourced from social media users. To address these challenges, the authors introduce a novel model, termed the Evidence-based AMR Attention Network (EA$^2$N). This model incorporates an Abstract Meaning Representation (AMR) graph and a refined knowledge graph derived from Wikidata to extract evidential features, while employing BERT to capture semantic features. Subsequently, these two sets of features are concatenated to predict the veracity labels. Experimental validation is conducted to demonstrate the model's effectiveness.

### Strengths
1. The paper focuses on a practical and challenging issue, fake news detection based on external evidence.
2. The model is the first attempt to utilize an AMR graph to enhance the detection of fake news.
3. The experiments are extensive, and significantly and consistently outperform the state-of-the-art model, which can prove the effectiveness of the proposed model.

### Weaknesses
However, despite the superior performance of the proposed model, there still exist some weaknesses in the paper. 
1. In the Introduction section, the authors summarize several problems in existing fake news detection (FND) works. However, the author seems not to have successfully solved all the problems.
2. AMR parser has been a well-studied technique used by a variety of NLP tasks. Therefore, the novelty of the idea of incorporating AMR into FND is limited.
3. This paper proposes a FND model that uses AMR and Wikidata knowledge. However, this method is not only suitable for the FND task, but can also be applied to other knowledge-rich NLP tasks, e.g. sentiment analysis and intent detection. So why do the authors only focus on the fake news detection task? In other words, which characteristics of EA$^2$N determine that this method is only suitable for fake news detection?
4. The sensitivity analysis of the thresholds $\gamma$ and $\delta$ should be provided.

**Other details:**
1. In order to ensure standardization, citations should be revised, e.g. Brewer et al. (2013) -> (Brewer et al. 2013).
2. The algorithm in Sec.3.3.1 involves being converted into a figure or a standard algorithm table for ease of understanding.

### Questions
1. AMR is a kind of graph to capture semantic correlations of documents. And dependency tree can play the same role with AMR. Therefore, what are the advantages of AMR compared to dependency trees?
2. As discussed in the Weakness part, whether this paper solves the problem *"the way of incorporating external knowledge into these models is not highly reliable and time-consuming."*

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces EA2N, an Evidence-based AMR Attention Network for Fake News Detection. The proposed framework leverages Abstract Meaning Representation (AMR) and incorporates knowledge from Wikidata to detect fake news. It combines language encoder and graph encoder to effectively capture complex semantic relations and improve the reliability of incorporating external knowledge. Their experiments demonstrate the effectiveness of EA2N compared to state-of-the-art methodologies.

### Strengths
- The paper is well-written and easy to follow. 
- The authors claim they will release the code once the discussion forum start.
- Compared with the baselines used in this paper, EA2N achive effective resuls.

### Weaknesses
 - The idea of use external knowledge to enhane fake news detection is not new.

### Questions
No

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an evidence-based AMR attention NN for fake news detection. The proposed framework encompasses a combination of language encoder and graph encoder to detect fake news using AMR and wiki external knowledge. The experimental results show the effectiveness of the proposed model.

### Strengths
The overall structure is well organized. The experimental results show the effectiveness of the wiki's external knowledge and AMR information. The ablation studies and case studies are reasonable.

### Weaknesses
The overall novelty of the method is not enough for the ICLR conference. The model is an ensemble and common usage (like transformer graph). There are some similar methods in other references. Evidence-aware Fake News Detection with Graph Neural Networks.  MUSER: A MUlti-Step Evidence Retrieval Enhancement Framework for Fake News Detection.  Detecting Out-of-Context Multimodal Misinformation with interpretable neural-symbolic model.

The ablation studies should add the ELF and CLF-based experiments to show the effectiveness. 

It's better to add more datasets about fake news detection, such as  Snop. 

The format of reference should be revised (Devlin et al., 2019)

### Questions
See aboove.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study introduces the $EA^2N$ model for binary fake news classification, leveraging external evidence. The model employs two parallel pipelines to represent news articles: text-based and graph-based.

In the graph-based pipeline, news text is transformed into an Abstract Meaning Representation (AMR) graph. Subsequently, an augmented AMR graph is constructed through entity linking, utilizing evidence paths from an external knowledge base, specifically the Wikidata5M graph. An $\mathcal{A}^*$ search over the Wikidata5M graph is used to identify evidence paths between corresponding entities in the AMR graph. These paths are then merged with the original AMR graph to create the augmented graph. Finally, a graph transformer is employed to learn representations from this augmented graph.

Concurrently, BERT (along with lexical features) is used to acquire textual representations. Ultimately, the learned representations from both pipelines are concatenated and input to a classification head. The $EA^2N$ model is evaluated on two datasets, outperforming the chosen baselines.

It's worth noting that this architectural approach combines various pre-existing elements, but the underlying rationale for several components is not explicitly detailed in the work, raising several concerns as highlighted in the "Questions" and "Weakness" sections.

### Strengths
- The authors provide an effective amalgamation of the graph- and text-based pipeline for learning representation (although not entirely novel).
- The figures and tables give a clear picture of the underlying model and experimentation.
- The authors perform the much required ablation studies.

### Weaknesses
The proposed architecture seems to be an attempt to combine several pre-existing architectures -- i.e. Language Encoder (BERT [6] + FakeFlow [7]), Path-aware Graph Learning Module (Graph Transformer [8]) and Graph Generation and Integration ($\mathcal{A}^*$ search with a TagMe API [9] -based heuristic). While these architectures have been amalgamated to propose a new model, these aren't *novel* contributions. The paper isn't well written (in some places) in the sense that several key notations are missing, and the narrative of the work could have been improved. All the baselines have been directly adopted from the FinerFact [5] paper. Such practices should be avoided. I have highlighted several weaknesses and concerns under the "Questions" section.


**Evidence Integration with AMR**: There seem to be several incomplete parts, which need to be explained.

---  In Entity-level Filtering $(\mathcal{R}^{(S,D)}_{ELF} = Relatedness(v_s^{wiki}, v_d^{wiki}))$, the authors have not mentioned what the $Relatedness(.)$ function is? Without an ***explicit*** definition of the function, it is diffiucult to assess the working of the ELF and CLF algorithms since the $Relatedness(.)$ function seems to be the "main" heuristic being used here.

- From a look at the Appendix, it seems (***implicitly***) that the authors use the TagMe API to compute the relatedness, but what "explicitly" is the function definition used?

--- The Figure 2 (and following text) mentions that the authors use $\mathcal{A}^*$ search on the Wiki-graph to find the (optimal) path between source $v_s^{amr}$ and destination $v_d^{amr}$. However the Algorithm 2 described as "Context-level Filtering" doesn't seem to represent $\mathcal{A}^*$ search.

- For $\mathcal{A}^*$ search, $f$ (total cost) = $g$ (current cost) + $h$ (heuristic approximation of the future cost). Here, $f$ (total cost) must be the criterion for choosing the next node in path. If we assume that, $h = \mathcal{R}^{(i,D)}_{CLF} = Relatedness(v_i^{wiki}, v_d^{wiki}) > \delta$ is the heuristic cost to reach the destination $d$ from $i$, what is $g$? The authors don't provide information for that. Incase $g$ is being ignored (or taken 0), it becomes a *greedy-heuristic* search, and not $\mathcal{A}^*$. 
- A possible $\mathcal{A}^*$ variant could have been:

$g + h = \mathcal{R}^{(S,i)}_{CLF} + \mathcal{R}^{(i,D)}_{CLF} = Relatedness(v_s^{wiki}, v_i^{wiki}) + Relatedness(v_i^{wiki}, v_d^{wiki}) > \delta*$


**Relation Encoder in Path-aware Graph Learning Module**: For every pair of entities $(v_s^{amr}, v_d^{amr})$ in $\mathcal{G}^{amr}$, two distinct sources of relational data exist in $\mathcal{G}^{WikiAMR}$: AMR-based relations and evidence-based relations from Wikidata:

- Using the notation from paper: $\mathcal{G}^{WikiAMR} = \mathcal{G}^{amr} \cup \sum_{s, d} \mathcal{P}^{wiki}(v_s^{amr}, v_d^{amr})$.
- Consider the shortest path denoted as $sp_{s \rightarrow d} = \set { e(v_s^{amr}, n_1), e(n_1, n_2), \dots, e(n_k, v_d^{amr})\}$ within $\mathcal{G}^{WikiAMR}$. Here, $e^{amr}$ represents an edge within $\mathcal{G}^{amr}$, and $e^{wiki}$ represents an edge within $\sum_{s, d} \mathcal{P}^{wiki}(v_s^{amr}, v_d^{amr})$. Therefore, the collective edge set $e^{WikiAMR} = e^{wiki} \cup e^{amr}$.
- Let $sp^{amr}_{s \rightarrow d} = \set {e^{amr}(v_s^{amr}, n_1), e^{amr}(n_1, n_2), \dots, e^{amr}(n_k, v_d^{amr})\}$ be the shortest path that relies solely on AMR-based relations (i.e., exclusively within $\mathcal{G}^{amr}$). Simultaneously, $sp^{wiki}_{s \rightarrow d} = \set {e^{wiki}(v_s^{amr}, n_1), \dots, e^{wiki}(n_k, v_d^{amr})\}$ represents the shortest path utilizing only evidence-based connections.
- As indicated by Table 2 and Figure 5, a significant portion of entities are linked through evidence-based connections with just one hop, meaning they are connected directly. In other words, for most entity pairs, the shortest path is the "direct" evidence path with a single edge originating from the Wiki graph. This can be represented as $sp_{s \rightarrow d} = sp^{wiki}_{s \rightarrow d} = \{ e^{wiki}(v_s^{amr}, v_d^{amr})\}$ (Because, as per Table 2, in most cases, the number of edges in $sp^{wiki}_{s \rightarrow d}$ (being 1 in majority cases), is less than or equal to that in $sp^{amr}_{s \rightarrow d}$.

In essence, this implies that in most cases, when encoding a relationship $r_{s \rightarrow d}$, the relation encoder would **overlook the AMR-based relation information**. While Wikidata relations are valuable, disregarding AMR-level relations may not be technically justified. Therefore, the authors should contemplate how to adapt the relation encoder in the graph transformer to effectively integrate both information sources.

**Abstract Meaning Representation**: I have a few major concerns about using an AMR representation here:

- The average length of news articles in the Gossipcop dataset is **~600 words** [2] (Some articles are as large as 1000 words). In the case of such large input length, the AMR graphs are going to be "very" noisy. How do the authors handle this case?
- The authors don't elaborate on the intuition behind using the Abstract Meaning Representation ("Why specificaly AMR?")? There can be other (more sophisticated) variants of AMR like **AMR-IE** [1] (which uses an AMR guided graph decoder to extract knowledge elements based on the order decided by the hierarchical structures in AMR) which seem more relevant owing to the "integration of external knowledge" used in this work. What about knowledge graphs other than AMR (eg. OpenIE-based approaches [3])?
- It seems that the authors have used an off-the-shelf pretrained AMR parser, however they have not provided any details about the same. Was the AMR parser finetuned? (I am guessing not!)

**Insufficient Experimentation**: 

- The presented results are exclusively based on two datasets, Politifact and Gossipcop, both of which are part of the FakeNewsNet database. To ensure the generalizability of the proposed architecture, it is essential for the authors to include results from additional datasets spanning various domains or social media platforms. Moreover, it's worth noting that Politifact, one of the datasets, contains only 815 news articles.
- Several of the selected baseline models do not provide a fair basis for comparison. For instance, GCAN [4] incorporates the propagation path of the tweet and user profiles in addition to the source tweet content, features not utilized by the proposed model.
- A logistical concern arises from the fact that all the baseline models and their results, including SVM, DTC, RFC, GRU-2, FF, B- TransE, KCNN, GCAN, and KAN, appear to **have been directly borrowed from the FinerFact** [5] paper. Such practices should be avoided, and the authors should explicitly mention the sources of these baseline models in their paper.
- In the ablation study examining different variants of the proposed model, such as LM, AMR, LE|AMR, and LE|WikiAMR, the authors should provide significance hypothesis test results (e.g., T-test) alongside the standard deviation of the metrics across multiple runs. Including these statistical measures would enhance the interpretability of the results.

### Questions
**Evidence Integration with AMR**: There seem to be several incomplete parts, which need to be explained.

---  In Entity-level Filtering $(\mathcal{R}^{(S,D)}_{ELF} = Relatedness(v_s^{wiki}, v_d^{wiki}))$, the authors have not mentioned what the $Relatedness(.)$ function is? Without an ***explicit*** definition of the function, it is diffiucult to assess the working of the ELF and CLF algorithms since the $Relatedness(.)$ function seems to be the "main" heuristic being used here.

- From a look at the Appendix, it seems (***implicitly***) that the authors use the TagMe API to compute the relatedness, but what "explicitly" is the function definition used? 

--- The Figure 2 (and following text) mentions that the authors use $\mathcal{A}^*$ search on the Wiki-graph to find the (optimal) path between source $v_s^{amr}$ and destination $v_d^{amr}$. However the Algorithm 2 described as "Context-level Filtering" doesn't seem to represent $\mathcal{A}^*$ search. 

- For $\mathcal{A}^*$ search, $f$ (total cost) = $g$ (current cost) + $h$ (heuristic approximation of the future cost). Here, $f$ (total cost) must be the criterion for choosing the next node in path. If we assume that, $h = \mathcal{R}^{(i,D)}_{CLF} = Relatedness(v_i^{wiki}, v_d^{wiki}) > \delta$ is the heuristic cost to reach the destination $d$ from $i$, what is $g$? The authors don't provide information for that. Incase $g$ is being ignored (or taken 0), it becomes a *greedy-heuristic* search, and not $\mathcal{A}^*$. 
- A possible $\mathcal{A}^*$ variant could have been:

$g + h = \mathcal{R}^{(S,i)}\_{CLF} + \mathcal{R}^{(i,D)}\_{CLF} = Relatedness(v_s^{wiki}, v_i^{wiki}) + Relatedness(v_i^{wiki}, v_d^{wiki}) > \delta*$


**Relation Encoder in Path-aware Graph Learning Module**: For every pair of entities $(v_s^{amr}, v_d^{amr})$ in $\mathcal{G}^{amr}$, two distinct sources of relational data exist in $\mathcal{G}^{WikiAMR}$: AMR-based relations and evidence-based relations from Wikidata:

- Using the notation from paper: $\mathcal{G}^{WikiAMR} = \mathcal{G}^{amr} \cup \sum_{s, d} \mathcal{P}^{wiki}(v_s^{amr}, v_d^{amr})$.
- Consider the shortest path denoted as $sp_{s \rightarrow d} = \set { e(v_s^{amr}, n_1), e(n_1, n_2), \dots, e(n_k, v_d^{amr})\}$ within $\mathcal{G}^{WikiAMR}$. Here, $e^{amr}$ represents an edge within $\mathcal{G}^{amr}$, and $e^{wiki}$ represents an edge within $\sum_{s, d} \mathcal{P}^{wiki}(v_s^{amr}, v_d^{amr})$. Therefore, the collective edge set $e^{WikiAMR} = e^{wiki} \cup e^{amr}$.
- Let $sp^{amr}\_{s \rightarrow d} = \set {e^{amr}(v_s^{amr}, n_1), e^{amr}(n_1, n_2), \dots, e^{amr}(n_k, v_d^{amr})\}$ be the shortest path that relies solely on AMR-based relations (i.e., exclusively within $\mathcal{G}^{amr}$). Simultaneously, $sp^{wiki}\_{s \rightarrow d} = \set {e^{wiki}(v_s^{amr}, n_1), \dots, e^{wiki}(n_k, v_d^{amr})}$ represents the shortest path utilizing only evidence-based connections.
- As indicated by Table 2 and Figure 5, a significant portion of entities are linked through evidence-based connections with just one hop, meaning they are connected directly. In other words, for most entity pairs, the shortest path is the "direct" evidence path with a single edge originating from the Wiki graph. This can be represented as $sp_{s \rightarrow d} = sp^{wiki}\_{s \rightarrow d} = \{ e^{wiki}(v_s^{amr}, v_d^{amr})\}$ (Because, as per Table 2, in most cases, the number of edges in $sp^{wiki}\_{s \rightarrow d}$ (being 1 in majority cases), is less than or equal to that in $sp^{amr}_{s \rightarrow d}$.

In essence, this implies that in most cases, when encoding a relationship $r_{s \rightarrow d}$, the relation encoder would **overlook the AMR-based relation information**. While Wikidata relations are valuable, disregarding AMR-level relations may not be technically justified. Therefore, the authors should contemplate how to adapt the relation encoder in the graph transformer to effectively integrate both information sources.

**Abstract Meaning Representation**: I have a few major concerns about using an AMR representation here:

- The average length of news articles in the Gossipcop dataset is **~600 words** [2] (Some articles are as large as 1000 words). In the case of such large input length, the AMR graphs are going to be "very" noisy. How do the authors handle this case?
- The authors don't elaborate on the intuition behind using the Abstract Meaning Representation ("Why specificaly AMR?")? There can be other (more sophisticated) variants of AMR like **AMR-IE** [1] (which uses an AMR guided graph decoder to extract knowledge elements based on the order decided by the hierarchical structures in AMR) which seem more relevant owing to the "integration of external knowledge" used in this work. What about knowledge graphs other than AMR (eg. OpenIE-based approaches [3])?
- It seems that the authors have used an off-the-shelf pretrained AMR parser, however they have not provided any details about the same. Was the AMR parser finetuned? (I am guessing not!)

**Insufficient Experimentation**: 

- The presented results are exclusively based on two datasets, Politifact and Gossipcop, both of which are part of the FakeNewsNet database. To ensure the generalizability of the proposed architecture, it is essential for the authors to include results from additional datasets spanning various domains or social media platforms. Moreover, it's worth noting that Politifact, one of the datasets, contains only 815 news articles.
- Several of the selected baseline models do not provide a fair basis for comparison. For instance, GCAN [4] incorporates the propagation path of the tweet and user profiles in addition to the source tweet content, features not utilized by the proposed model.
- A logistical concern arises from the fact that all the baseline models and their results, including SVM, DTC, RFC, GRU-2, FF, B- TransE, KCNN, GCAN, and KAN, appear to **have been directly borrowed from the FinerFact** [5] paper. Such practices should be avoided, and the authors should explicitly mention the sources of these baseline models in their paper.
- In the ablation study examining different variants of the proposed model, such as LM, AMR, LE|AMR, and LE|WikiAMR, the authors should provide significance hypothesis test results (e.g., T-test) alongside the standard deviation of the metrics across multiple runs. Including these statistical measures would enhance the interpretability of the results.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

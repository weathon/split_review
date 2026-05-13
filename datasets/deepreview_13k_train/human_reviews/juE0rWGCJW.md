# EX-Graph: A Pioneering Dataset Bridging Ethereum and X

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
While numerous public blockchain datasets are available, their utility is constrained by an exclusive focus on blockchain data. This constraint limits the incorporation of relevant social network data into blockchain analysis, thereby diminishing the breadth and depth of insight that can be derived.
To address the above limitation, we introduce EX-Graph, a novel dataset that authentically links Ethereum and X, marking the first and largest dataset of its kind. EX-Graph combines Ethereum transaction records (2 million nodes and 30 million edges) and X following data (1 million nodes and 3 million edges),  bonding 30,667 Ethereum addresses with verified X accounts sourced from OpenSea. Detailed statistical analysis on EX-Graph highlights the structural differences between X-matched and non-X-matched Ethereum addresses. Extensive experiments, including Ethereum link prediction, wash-trading Ethereum addresses detection, and X-Ethereum matching link prediction, emphasize the significant role of X data in enhancing Ethereum analysis. EX-Graph is available at \url{https://exgraph.deno.dev/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper delves into the analysis of Ethereum activities, specifically examining the influence of Twitter data on these activities. Through experiments, the authors compare the outcomes of Ethereum link predictions and wash-trading address detections with and without the integration of Twitter features. Their findings suggest that incorporating Twitter data can significantly enhance the performance of various graph-based models in these tasks. The research leverages advanced computational tools and the ETGraph dataset, emphasizing the potential synergy between blockchain activities and social media data.

### Strengths
The paper provides a new dataset for graph representation with Ethereum blockchain and Twitter data. As there are already existing datasets for the separated dataset, the combined dataset with opensea may be considered a contribution. The authors experimentally proved that combining the dataset improved the performance of Ethereum link prediction and wash trading detection using various existing methods. 
The novel dataset could be used in both the blockchain and ML communities to compete with SOTA for graph learning algorithms.

### Weaknesses
As the paper suggests a new dataset, it is acknowledged that the technical novelty is not strong enough. But as the authors provide a webpage and github page to easily use the dataset, it may contribute to the ML community.

### Questions
No questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper constructs a new graph dataset which uses Ethereum NFT transaction records together with Twitter social network. With the information from Twitter graph, the authors use BERT and deep walk to extract semantic and topology information, which is used as node feature for node on Ethereum graph. They conduct experiments on link prediction, wash-trading addresses detection, and matching link prediction tasks, demonstrating with the help of twitter features, various kinds of GNN methods can get performance improvements on all these tasks.

### Strengths
1. The paper proposes a novel idea to link Twitter social network to Ethereum networks which can provide node features for Ethereum networks.
2. Experiments are conducted thoroughly and prove that with Twitter features, most kinds of models can achieve better performance. Dataset statistics are provided clearly.

### Weaknesses
1. Though the title says ‘bridging Ethereum and Twitter’, the proposed dataset is focused on NFT transactions and related Twitter accounts. This scope is narrower than the title suggests. The authors should either demonstrate the dataset's applicability to other types of matching links beyond NFTs, such as identifying phishing or hack-related Ethereum addresses and their corresponding Twitter accounts, or they should revise the title to more accurately reflect the dataset's specific focus on NFTs. A more precise title would better manage reader expectations and highlight the specific contribution of this work.

2. In Section 3.3, the authors claim to obtain embeddings for all Twitter accounts using the DeepWalk algorithm, and Figure 2 indicates the use of structural features derived from DeepWalk. However, Appendix C.1 only mentions the use of 8 handcrafted features. This discrepancy needs clarification. If DeepWalk embeddings are indeed used, details about their generation, dimensionality, and integration with the handcrafted features should be provided in Appendix C.1. If DeepWalk is not used, Section 3.3 and Figure 2 should be revised to avoid misleading the reader.

3. For task 1, the link prediction task, the authors exclusively use matched addresses. While this is a valid starting point, it doesn't fully leverage the potential of GNNs to propagate information across the graph. Specifically, the authors should investigate how the inclusion of semantic information from Twitter impacts the prediction of links between non-matched Ethereum addresses. Since GNNs can pass node features via message-passing, the semantic information from matched nodes could potentially influence the predictions for non-matched nodes. An experiment exploring this aspect would provide a more comprehensive understanding of the dataset's utility and the effectiveness of the Twitter-derived features.

4. Task 3 aims to predict connections between Ethereum addresses and Twitter accounts. However, the methodology for handling negative samples raises concerns. Appendix K states that Twitter accounts without matched Ethereum addresses have an eight-dimensional zero-vector appended to their features. Section 4.4 describes negative samples as non-existing connections between Ethereum addresses and their matched Twitter accounts. This creates a potential bias. If negative samples include Twitter accounts without any profile information (represented by the zero-vector), the model might learn to trivially identify these accounts, leading to inflated performance metrics. A clearer definition of negative samples and a discussion of potential biases are necessary. It is unclear whether negative samples consist solely of Ethereum addresses paired with unmatched Twitter accounts or if they also include pairs of matched Ethereum addresses with incorrect Twitter accounts.

### Questions
See the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper contributes a dataset, termed ETGraph, that links Ethereum addresses with Twitter accounts. The dataset is structured in the form of a heterogeneous graph and inlcudes links between pairs of Ethereum addresses that transact with each other, links between Twitter accounts that follow/are followed by each other and links between Ethereum addresses and Twitter accounts that have been matched to be owned by the same (typically, physical) entity/person. This information has been scraped from opensea and the public Twitter API. The dataset also includes information about (a relatively small number of) money-laundering addresses. 

In addition, the paper also evaluates the dataset over a series of benchmark Graph Neural Network (GNN) models. Specifically, it compares whether the new dataset (with Twitter data) improves the ability of the models to predict Q1) links between Ethereum addresses, i.e., transactions, Q2) money laundering addresses, and Q3) matches between Ethereum addresses and Twitter accounts. With few exceptions, most evaluations suggest improved performance - at average levels around 6%-8% (maybe higher in some cases/lower in others) - with the new dataset in a couple of standard metrics including ROC, AUC, precision, recall and F1 scores.

### Strengths
- The dataset is novel and nicely connects Ethereum data to Twitter data. It involves a lot of hard work to put this dataset together and bring it to the heterogeneous graph structure. This is likely to have an impact (be useful) to researchers in the blockchain field.
- Regarding reproducibility, the paper is transparent and I could verify the links to the provided datasets and code.
- The evaluations indicate generally improved performance for a wide range of benchmark GNN models.

### Weaknesses
 - The paper is not self-contained and a lot of things need to be assessed through the external links to the dataset or through the appendix. I am not very familiar with dataset papers, so maybe this is generally so. 
- For this reason, I cannot comment on the ethical considerations about releasing such a dataset. 
- Q2 in the evaluation seems to make no sense to me: since there are only 3 matched addresses in the dataset, why should we anticipate improved performance with this dataset? The results are, thus, questionable to me regarding Q2. 
- The insight that Twitter-matched addresses are more active in Ethereum is rather expected since Twitter is known to be popular (as the authors also confirm) by main actors of the Ethereum ecosystem. 
- On a subjective comment, I am not sure if ICLR is the right venue to maximize visibility for this type of datasets. However, Chartalist, a recent publication in NeurIPS about a related blockchain dataset seems to suggest the contrary. Also, related to my comment about ethical considerations above, the authors seem to have followed the related discussion on openreview about Charalist and have included statements in the appendix. However, I am not in a position to assess those, because I am not aware of the exact regulations regarding such datasets. For this reason, I raise a flag for ethics review below - but I would be happy to take it down if this is clarified.
- There are some technical things that I discuss below, but these seems to be more minor in nature. As an example, the set of features degree (3 features) and neighbor (3 features) seem to be highly linearly correlated (as also suggested by their statistics in Table 3). Keeping only of them, i.e., one from the "degree" family, and one from the "neighbor" family, would potentially improve the performance of the networks. I provide a couple of more minor comments below.

### Questions
- Can you please discuss the weaknesses above?
- Is overs-smoothing a relevant problem in the evaulations and if yes, have you taken steps to address it?

Minor:
- Figure 2: In the Feature Extraction column, we read in the first box "Degree"-> Structural Features. So, here, you mean that look at the degree of the node or that "Degree" is some kind of network like BERT and Deepwalk in the next two boxes of that column? I found this slightly confusing. Also, which structural features are extracted here since ETH addresses don't contain any further information.
- Below Figure 2: "The total collection accounts for 30,387 Twitter profiles". I was confused here: why is this lower than the initial number (since, according to the previous lines more data was added) and why are Followers and Friends useful here? Friends are not discussed elsewhere if I am not wrong.

Trivia: 
- should it be Twitter or X :)? 
- is it 19 billion or 190 billion as of September 23, the market value for Ethereum (page 1)? 
- please define abbreviations the first time that they are used, e.g., AUC.

Note on my score: although I rated the paper as slightly above the acceptance threshold, I may decrease my score if my concerns are not addressed. I also hope that through the discussion, I will be able to increase my confidence.

**Post-rebuttal**: Based on the authors' response, I raised my score to 8. I cannot remove the ethics flag, but, I believe that the authors have addressed this concern. I will not increase my confidence, since datasets is not my exact area of expertise - although, I am fairly confident that this dataset will be useful to blockchain research.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

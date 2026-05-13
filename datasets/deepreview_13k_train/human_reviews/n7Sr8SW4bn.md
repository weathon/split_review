# Mayfly: a Neural Data Structure for Graph Stream Summarization

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
A graph is a structure made up of vertices and edges used to represent complex relationships between entities, while a graph stream is a continuous flow of graph updates that convey evolving relationships between entities. The massive volume and high dynamism of graph streams promote research on data structures of graph summarization, which provides a concise and approximate view of graph streams with sub-linear space and linear construction time, enabling real-time graph analytics in various domains, such as social networking, financing, and cybersecurity.
In this work, we propose the Mayfly, the first neural data structure for summarizing graph streams. The Mayfly replaces handcrafted data structures with better accuracy and adaptivity.
To cater to practical applications, Mayfly incorporates two offline training phases.
During the larval phase, the Mayfly learns basic summarization abilities from automatically and synthetically constituted meta-tasks, and in the metamorphosis phase, it rapidly adapts to real graph streams via meta-tasks.
With specific configurations of information pathways, the Mayfly enables flexible support for miscellaneous graph queries, including edge, node, and connectivity queries.
Extensive empirical studies show that the Mayfly significantly outperforms its handcrafted competitors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a Mayfly framework consisting of two stages (larval and metamorphosis) for summarizing graph streams. It is the first neural data structure for graph stream summarization. The Mayfly acquires basic summarization capabilities by learning from synthetic data and can be rapidly adapted to real graph streams. The Mayfly framework is agile and customizable, supporting a broad range of graph queries with lightweight information pathway configurations.

### Strengths
S1: The authors' integration of Mayfly with machine learning is interesting.
S2: Well-written.

### Weaknesses
W1: It seems that this paper leans more towards an engineering-oriented research, and its technology appears to be quite fundamental. For instance, it utilizes techniques like meta-learning and follows the paradigm of pre-training and fine-tuning. In my view, there's very little innovation at the model level, which is the most fundamental reason for my minor rejection.
W2: The authors' integration of graph streams with the Mayfly framework is indeed intriguing. However, from my perspective, it appears to be a fundamental application of pre-training and fine-tuning methods. I believe the authors should provide a clear explanation in the introduction or methodology section regarding why the Mayfly framework is particularly suitable for adapting to graph data streams.
W3: While the authors propose the Mayfly framework with the aim of enhancing data stream processing efficiency, I did not see a clear experimental demonstration of its efficiency gains. In other words, I would appreciate a more tangible comparison between the Mayfly framework and the comparative algorithms in terms of actual runtime efficiency under the same spatial budget.

### Questions
Please refer to weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a neural data structure for graph stream summarization, which has neatly designed modules (representation, addressing and decoding), as well as corresponding operations such as store and multiple types of queries. Experiments on Lkml and Enron datasets demonstrate the superiority of the designed approach compared to the SOTA TCM and GSS baselines.

### Strengths
1. The paper studies an interesting topic on using neural data structure for graph stream summarization, and designed the approach very neatly. In general, the presentation of the methodology is very clear and makes it easier to understand the nontrivial details.

2. The training strategy is inspiring, following the paradigm of "pre-training and fine-tuning", and thus has two stages called larval phase and metamorphosis phase.

3. Comprehensive experimental results demonstrate both the effectiveness of the method on different types of queries and throughputs.

### Weaknesses
1. Minor: A table of dataset statistics is suggested to make it more straightforward.


### Questions
1. In addition to throughput, is there any other metric to evaluate the efficiency of the method (e.g., query time)?
2. How to balance between the parameter size and model accuracy?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors utilize memory-augmented networks for summarizing graph streams into a fixed space. Given the compressed result and a specific edge (or a subset of edges), one can approximate the edge's weight. The neural network is first pre-trained on synthetic graph streams and later fine-tuned using a fraction of the input stream. When compared to sketching-based approaches, the suggested method shows a better approximation accuracy for a given compression size.

### Strengths
S1. The overall design of the suggested proposed, particularly the use of memory-augmented networks for compressing graph streams, seems reasonable.

S2. The introduced method exhibits significant improvements compared to sketching-based approaches.

S3. The proposed successfully applies to billion-scale graphs, highlighting its practicality for real-world scenarios.

### Weaknesses
W1. The paper lacks a theoretical analysis of complexity and accuracy.

W2. The presentation could be clearer. The insights and novelties of the addressing, decoding, and store operations could be specified. Specifically, the description of the addressing scheme lacks detail regarding how the 2D separated in/out-degree scheme is implemented and how it differs from existing approaches. The storage mechanism, which jointly compresses nodes and edges, also requires further clarification on the specific compression techniques used and the rationale behind this joint approach. The decoding process needs a more in-depth explanation of how altering information pathways in memory networks is achieved and how this enables multi-decoding for different query types.

W3. The proposed method seems to only support weight-related queries, not graph algorithms like Dijkstra’s.

W4. While somewhat expected, the throughput of the proposed method is not as high as that of rule-based baseline methods.

### Questions
Q1. Can complex graph algorithms, like Dijkstra's, be executed using the summary? If they can, does it substantially impact the time complexity compared to executing the algorithms on the uncompressed graph?

Q2.  Can you provide a more detailed explanation of how the MiGain term contributes? The present explanation seems too concise.

Q3. What is the time complexity of the addressing, decoding, and store operations?

Q4. The reported ARE and AAE seem quite large. What are their values when we use the mean as the estimate of all edge weights?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

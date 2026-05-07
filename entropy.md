

{0}------------------------------------------------

# A Mathematical Theory of Communication

By C. E. SHANNON

## INTRODUCTION

THE recent development of various methods of modulation such as PCM and PPM which exchange bandwidth for signal-to-noise ratio has intensified the interest in a general theory of communication. A basis for such a theory is contained in the important papers of Nyquist<sup>1</sup> and Hartley<sup>2</sup> on this subject. In the present paper we will extend the theory to include a number of new factors, in particular the effect of noise in the channel, and the savings possible due to the statistical structure of the original message and due to the nature of the final destination of the information.

The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. Frequently the messages have *meaning*; that is they refer to or are correlated according to some system with certain physical or conceptual entities. These semantic aspects of communication are irrelevant to the engineering problem. The significant aspect is that the actual message is one *selected from a set* of possible messages. The system must be designed to operate for each possible selection, not just the one which will actually be chosen since this is unknown at the time of design.

If the number of messages in the set is finite then this number or any monotonic function of this number can be regarded as a measure of the information produced when one message is chosen from the set, all choices being equally likely. As was pointed out by Hartley the most natural choice is the logarithmic function. Although this definition must be generalized considerably when we consider the influence of the statistics of the message and when we have a continuous range of messages, we will in all cases use an essentially logarithmic measure.

The logarithmic measure is more convenient for various reasons:

1. It is practically more useful. Parameters of engineering importance such as time, bandwidth, number of relays, etc., tend to vary linearly with the logarithm of the number of possibilities. For example, adding one relay to a group doubles the number of possible states of the relays. It adds 1 to the base 2 logarithm of this number. Doubling the time roughly squares the number of possible messages, or doubles the logarithm, etc.
2. It is nearer to our intuitive feeling as to the proper measure. This is closely related to (1) since we intuitively measure entities by linear comparison with common standards. One feels, for example, that two punched cards should have twice the capacity of one for information storage, and two identical channels twice the capacity of one for transmitting information.
3. It is mathematically more suitable. Many of the limiting operations are simple in terms of the logarithm but would require clumsy restatement in terms of the number of possibilities.

The choice of a logarithmic base corresponds to the choice of a unit for measuring information. If the base 2 is used the resulting units may be called binary digits, or more briefly *bits*, a word suggested by J. W. Tukey. A device with two stable positions, such as a relay or a flip-flop circuit, can store one bit of information.  $N$  such devices can store  $N$  bits, since the total number of possible states is  $2^N$  and  $\log_2 2^N = N$ . If the base 10 is used the units may be called decimal digits. Since

$$\begin{aligned}\log_2 M &= \log_{10} M / \log_{10} 2 \\ &= 3.32 \log_{10} M,\end{aligned}$$

<sup>1</sup>Nyquist, H., "Certain Factors Affecting Telegraph Speed," *Bell System Technical Journal*, April 1924, p. 324; "Certain Topics in Telegraph Transmission Theory," *A.I.E.E. Trans.*, v. 47, April 1928, p. 617.

<sup>2</sup>Hartley, R. V. L., "Transmission of Information," *Bell System Technical Journal*, July 1928, p. 535.

{1}------------------------------------------------

![Schematic diagram of a general communication system. The diagram shows a linear flow from left to right: INFORMATION SOURCE (producing a MESSAGE) to TRANSMITTER (producing a SIGNAL). The SIGNAL is transmitted through a channel where it is affected by a NOISE SOURCE (added from below). The result is a RECEIVED SIGNAL, which is then processed by a RECEIVER (producing a MESSAGE) and finally reaching the DESTINATION.](68ac34ff111db52afaa786afcb8346c3_img.jpg)

```

graph LR
    IS[INFORMATION SOURCE] -- MESSAGE --> T[TRANSMITTER]
    T -- SIGNAL --> C(( ))
    NS[NOISE SOURCE] --> C
    C -- RECEIVED SIGNAL --> R[RECEIVER]
    R -- MESSAGE --> D[DESTINATION]
  
```

Schematic diagram of a general communication system. The diagram shows a linear flow from left to right: INFORMATION SOURCE (producing a MESSAGE) to TRANSMITTER (producing a SIGNAL). The SIGNAL is transmitted through a channel where it is affected by a NOISE SOURCE (added from below). The result is a RECEIVED SIGNAL, which is then processed by a RECEIVER (producing a MESSAGE) and finally reaching the DESTINATION.

Fig. 1—Schematic diagram of a general communication system.

a decimal digit is about  $3\frac{1}{3}$  bits. A digit wheel on a desk computing machine has ten stable positions and therefore has a storage capacity of one decimal digit. In analytical work where integration and differentiation are involved the base  $e$  is sometimes useful. The resulting units of information will be called natural units. Change from the base  $a$  to base  $b$  merely requires multiplication by  $\log_b a$ .

By a communication system we will mean a system of the type indicated schematically in Fig. 1. It consists of essentially five parts:

1. An *information source* which produces a message or sequence of messages to be communicated to the receiving terminal. The message may be of various types: (a) A sequence of letters as in a telegraph of teletype system; (b) A single function of time  $f(t)$  as in radio or telephony; (c) A function of time and other variables as in black and white television — here the message may be thought of as a function  $f(x, y, t)$  of two space coordinates and time, the light intensity at point  $(x, y)$  and time  $t$  on a pickup tube plate; (d) Two or more functions of time, say  $f(t)$ ,  $g(t)$ ,  $h(t)$  — this is the case in “three-dimensional” sound transmission or if the system is intended to service several individual channels in multiplex; (e) Several functions of several variables — in color television the message consists of three functions  $f(x, y, t)$ ,  $g(x, y, t)$ ,  $h(x, y, t)$  defined in a three-dimensional continuum — we may also think of these three functions as components of a vector field defined in the region — similarly, several black and white television sources would produce “messages” consisting of a number of functions of three variables; (f) Various combinations also occur, for example in television with an associated audio channel.
2. A *transmitter* which operates on the message in some way to produce a signal suitable for transmission over the channel. In telephony this operation consists merely of changing sound pressure into a proportional electrical current. In telegraphy we have an encoding operation which produces a sequence of dots, dashes and spaces on the channel corresponding to the message. In a multiplex PCM system the different speech functions must be sampled, compressed, quantized and encoded, and finally interleaved properly to construct the signal. Vocoder systems, television and frequency modulation are other examples of complex operations applied to the message to obtain the signal.
3. The *channel* is merely the medium used to transmit the signal from transmitter to receiver. It may be a pair of wires, a coaxial cable, a band of radio frequencies, a beam of light, etc.
4. The *receiver* ordinarily performs the inverse operation of that done by the transmitter, reconstructing the message from the signal.
5. The *destination* is the person (or thing) for whom the message is intended.

We wish to consider certain general problems involving communication systems. To do this it is first necessary to represent the various elements involved as mathematical entities, suitably idealized from their

{2}------------------------------------------------

physical counterparts. We may roughly classify communication systems into three main categories: discrete, continuous and mixed. By a discrete system we will mean one in which both the message and the signal are a sequence of discrete symbols. A typical case is telegraphy where the message is a sequence of letters and the signal a sequence of dots, dashes and spaces. A continuous system is one in which the message and signal are both treated as continuous functions, e.g., radio or television. A mixed system is one in which both discrete and continuous variables appear, e.g., PCM transmission of speech.

We first consider the discrete case. This case has applications not only in communication theory, but also in the theory of computing machines, the design of telephone exchanges and other fields. In addition the discrete case forms a foundation for the continuous and mixed cases which will be treated in the second half of the paper.

## PART I: DISCRETE NOISELESS SYSTEMS

### 1. THE DISCRETE NOISELESS CHANNEL

Teletype and telegraphy are two simple examples of a discrete channel for transmitting information. Generally, a discrete channel will mean a system whereby a sequence of choices from a finite set of elementary symbols  $S_1, \dots, S_n$  can be transmitted from one point to another. Each of the symbols  $S_i$  is assumed to have a certain duration in time  $t_i$  seconds (not necessarily the same for different  $S_i$ , for example the dots and dashes in telegraphy). It is not required that all possible sequences of the  $S_i$  be capable of transmission on the system; certain sequences only may be allowed. These will be possible signals for the channel. Thus in telegraphy suppose the symbols are: (1) A dot, consisting of line closure for a unit of time and then line open for a unit of time; (2) A dash, consisting of three time units of closure and one unit open; (3) A letter space consisting of, say, three units of line open; (4) A word space of six units of line open. We might place the restriction on allowable sequences that no spaces follow each other (for if two letter spaces are adjacent, it is identical with a word space). The question we now consider is how one can measure the capacity of such a channel to transmit information.

In the teletype case where all symbols are of the same duration, and any sequence of the 32 symbols is allowed the answer is easy. Each symbol represents five bits of information. If the system transmits  $n$  symbols per second it is natural to say that the channel has a capacity of  $5n$  bits per second. This does not mean that the teletype channel will always be transmitting information at this rate — this is the maximum possible rate and whether or not the actual rate reaches this maximum depends on the source of information which feeds the channel, as will appear later.

In the more general case with different lengths of symbols and constraints on the allowed sequences, we make the following definition:

Definition: The capacity  $C$  of a discrete channel is given by

$$C = \lim_{T \rightarrow \infty} \frac{\log N(T)}{T}$$

where  $N(T)$  is the number of allowed signals of duration  $T$ .

It is easily seen that in the teletype case this reduces to the previous result. It can be shown that the limit in question will exist as a finite number in most cases of interest. Suppose all sequences of the symbols  $S_1, \dots, S_n$  are allowed and these symbols have durations  $t_1, \dots, t_n$ . What is the channel capacity? If  $N(t)$  represents the number of sequences of duration  $t$  we have

$$N(t) = N(t - t_1) + N(t - t_2) + \dots + N(t - t_n).$$

The total number is equal to the sum of the numbers of sequences ending in  $S_1, S_2, \dots, S_n$  and these are  $N(t - t_1), N(t - t_2), \dots, N(t - t_n)$ , respectively. According to a well-known result in finite differences,  $N(t)$  is then asymptotic for large  $t$  to  $X_0^t$  where  $X_0$  is the largest real solution of the characteristic equation:

$$X^{-t_1} + X^{-t_2} + \dots + X^{-t_n} = 1$$

{3}------------------------------------------------

and therefore

$$C = \log X_0.$$

In case there are restrictions on allowed sequences we may still often obtain a difference equation of this type and find  $C$  from the characteristic equation. In the telegraphy case mentioned above

$$N(t) = N(t-2) + N(t-4) + N(t-5) + N(t-7) + N(t-8) + N(t-10)$$

as we see by counting sequences of symbols according to the last or next to the last symbol occurring. Hence  $C$  is  $-\log \mu_0$  where  $\mu_0$  is the positive root of  $1 = \mu^2 + \mu^4 + \mu^5 + \mu^7 + \mu^8 + \mu^{10}$ . Solving this we find  $C = 0.539$ .

A very general type of restriction which may be placed on allowed sequences is the following: We imagine a number of possible states  $a_1, a_2, \dots, a_m$ . For each state only certain symbols from the set  $S_1, \dots, S_n$  can be transmitted (different subsets for the different states). When one of these has been transmitted the state changes to a new state depending both on the old state and the particular symbol transmitted. The telegraph case is a simple example of this. There are two states depending on whether or not a space was the last symbol transmitted. If so, then only a dot or a dash can be sent next and the state always changes. If not, any symbol can be transmitted and the state changes if a space is sent, otherwise it remains the same. The conditions can be indicated in a linear graph as shown in Fig. 2. The junction points correspond to the

![Figure 2: Graphical representation of the constraints on telegraph symbols. The diagram shows two states represented by junction points. The left state has two outgoing arrows: 'DASH' (top) and 'DOT' (bottom). The right state has two self-loops: 'DOT' (top) and 'DASH' (bottom). There are two curved arrows connecting the left and right states: 'LETTER SPACE' (top, left to right) and 'WORD SPACE' (bottom, right to left).](12a6537c92844d5b393104c02e8dfc2f_img.jpg)

Figure 2: Graphical representation of the constraints on telegraph symbols. The diagram shows two states represented by junction points. The left state has two outgoing arrows: 'DASH' (top) and 'DOT' (bottom). The right state has two self-loops: 'DOT' (top) and 'DASH' (bottom). There are two curved arrows connecting the left and right states: 'LETTER SPACE' (top, left to right) and 'WORD SPACE' (bottom, right to left).

Fig. 2—Graphical representation of the constraints on telegraph symbols.

states and the lines indicate the symbols possible in a state and the resulting state. In Appendix 1 it is shown that if the conditions on allowed sequences can be described in this form  $C$  will exist and can be calculated in accordance with the following result:

*Theorem 1: Let  $b_{ij}^{(s)}$  be the duration of the  $s^{\text{th}}$  symbol which is allowable in state  $i$  and leads to state  $j$ . Then the channel capacity  $C$  is equal to  $\log W$  where  $W$  is the largest real root of the determinant equation:*

$$\left| \sum_s W^{-b_{ij}^{(s)}} - \delta_{ij} \right| = 0$$

where  $\delta_{ij} = 1$  if  $i = j$  and is zero otherwise.

For example, in the telegraph case (Fig. 2) the determinant is:

$$\begin{vmatrix} -1 & (W^{-2} + W^{-4}) \\ (W^{-3} + W^{-6}) & (W^{-2} + W^{-4} - 1) \end{vmatrix} = 0.$$

On expansion this leads to the equation given above for this case.

### 2. THE DISCRETE SOURCE OF INFORMATION

We have seen that under very general conditions the logarithm of the number of possible signals in a discrete channel increases linearly with time. The capacity to transmit information can be specified by giving this rate of increase, the number of bits per second required to specify the particular signal used.

We now consider the information source. How is an information source to be described mathematically, and how much information in bits per second is produced in a given source? The main point at issue is the effect of statistical knowledge about the source in reducing the required capacity of the channel, by the use

{4}------------------------------------------------

of proper encoding of the information. In telegraphy, for example, the messages to be transmitted consist of sequences of letters. These sequences, however, are not completely random. In general, they form sentences and have the statistical structure of, say, English. The letter E occurs more frequently than Q, the sequence TH more frequently than XP, etc. The existence of this structure allows one to make a saving in time (or channel capacity) by properly encoding the message sequences into signal sequences. This is already done to a limited extent in telegraphy by using the shortest channel symbol, a dot, for the most common English letter E; while the infrequent letters, Q, X, Z are represented by longer sequences of dots and dashes. This idea is carried still further in certain commercial codes where common words and phrases are represented by four- or five-letter code groups with a considerable saving in average time. The standardized greeting and anniversary telegrams now in use extend this to the point of encoding a sentence or two into a relatively short sequence of numbers.

We can think of a discrete source as generating the message, symbol by symbol. It will choose successive symbols according to certain probabilities depending, in general, on preceding choices as well as the particular symbols in question. A physical system, or a mathematical model of a system which produces such a sequence of symbols governed by a set of probabilities, is known as a stochastic process.<sup>3</sup> We may consider a discrete source, therefore, to be represented by a stochastic process. Conversely, any stochastic process which produces a discrete sequence of symbols chosen from a finite set may be considered a discrete source. This will include such cases as:

1. Natural written languages such as English, German, Chinese.
2. Continuous information sources that have been rendered discrete by some quantizing process. For example, the quantized speech from a PCM transmitter, or a quantized television signal.
3. Mathematical cases where we merely define abstractly a stochastic process which generates a sequence of symbols. The following are examples of this last type of source.
 - (A) Suppose we have five letters A, B, C, D, E which are chosen each with probability .2, successive choices being independent. This would lead to a sequence of which the following is a typical example.
 

B D C B C E C C C A D C B D D A A E C E E A  
A B B D A E E C A C E E B A E E C B C E A D.

 This was constructed with the use of a table of random numbers.<sup>4</sup>
 - (B) Using the same five letters let the probabilities be .4, .1, .2, .2, .1, respectively, with successive choices independent. A typical message from this source is then:
 

A A A C D C B D C E A A D A D A C E D A  
E A D C A B E D A D D C E C A A A A A D.
 - (C) A more complicated structure is obtained if successive symbols are not chosen independently but their probabilities depend on preceding letters. In the simplest case of this type a choice depends only on the preceding letter and not on ones before that. The statistical structure can then be described by a set of transition probabilities  $p_i(j)$ , the probability that letter  $i$  is followed by letter  $j$ . The indices  $i$  and  $j$  range over all the possible symbols. A second equivalent way of specifying the structure is to give the “digram” probabilities  $p(i, j)$ , i.e., the relative frequency of the digram  $i j$ . The letter frequencies  $p(i)$ , (the probability of letter  $i$ ), the transition probabilities

<sup>3</sup>See, for example, S. Chandrasekhar, “Stochastic Problems in Physics and Astronomy,” *Reviews of Modern Physics*, v. 15, No. 1, January 1943, p. 1.

<sup>4</sup>Kendall and Smith, *Tables of Random Sampling Numbers*, Cambridge, 1939.

{5}------------------------------------------------

$p_i(j)$  and the digram probabilities  $p(i, j)$  are related by the following formulas:

$$p(i) = \sum_j p(i, j) = \sum_j p(j, i) = \sum_j p(j) p_i(j)$$

$$p(i, j) = p(i) p_i(j)$$

$$\sum_j p_i(j) = \sum_i p(i) = \sum_{i,j} p(i, j) = 1.$$

As a specific example suppose there are three letters A, B, C with the probability tables:

| $p_i(j)$ | $j$ |  |  | $i$ | $p(i)$ | $p(i, j)$ | $j$ |  |  |
|-|-|-|-|-|-|-|-|-|-|
|  | A | B | C |  |  |  | A | B | C |
| A | 0 | $\frac{4}{3}$ | $\frac{1}{3}$ | A | $\frac{9}{27}$ | A | 0 | $\frac{4}{15}$ | $\frac{1}{15}$ |
| B | $\frac{1}{2}$ | $\frac{1}{2}$ | 0 | B | $\frac{16}{27}$ | B | $\frac{8}{27}$ | $\frac{4}{27}$ | 0 |
| C | $\frac{1}{2}$ | $\frac{2}{5}$ | $\frac{1}{10}$ | C | $\frac{2}{27}$ | C | $\frac{1}{27}$ | $\frac{4}{135}$ | $\frac{1}{135}$ |

A typical message from this source is the following:

A B B A B A B A B A B A B B A B B B B B A B A B A B A B B B A C A C A B  
 B A B B B A B B A B A C B B B A B A.

The next increase in complexity would involve trigram frequencies but no more. The choice of a letter would depend on the preceding two letters but not on the message before that point. A set of trigram frequencies  $p(i, j, k)$  or equivalently a set of transition probabilities  $p_{ij}(k)$  would be required. Continuing in this way one obtains successively more complicated stochastic processes. In the general  $n$ -gram case a set of  $n$ -gram probabilities  $p(i_1, i_2, \dots, i_n)$  or of transition probabilities  $p_{i_1, i_2, \dots, i_{n-1}}(i_n)$  is required to specify the statistical structure.

- (D) Stochastic processes can also be defined which produce a text consisting of a sequence of “words.” Suppose there are five letters A, B, C, D, E and 16 “words” in the language with associated probabilities:

|  |  |  |  |
|-|-|-|-|
| .10 A | .16 BEBE | .11 CABED | .04 DEB |
| .04 ADEB | .04 BED | .05 CEED | .15 DEED |
| .05 ADEE | .02 BEED | .08 DAB | .01 EAB |
| .01 BADD | .05 CA | .04 DAD | .05 EE |

Suppose successive “words” are chosen independently and are separated by a space. A typical message might be:

DAB EE A BEBE DEED DEB ADEE ADEE EE DEB BEBE BEBE BEBE ADEE BED DEED  
 DEED CEED ADEE A DEED DEED BEBE CABED BEBE BED DAB DEED ADEB.

If all the words are of finite length this process is equivalent to one of the preceding type, but the description may be simpler in terms of the word structure and probabilities. We may also generalize here and introduce transition probabilities between words, etc.

These artificial languages are useful in constructing simple problems and examples to illustrate various possibilities. We can also approximate to a natural language by means of a series of simple artificial languages. The zero-order approximation is obtained by choosing all letters with the same probability and independently. The first-order approximation is obtained by choosing successive letters independently but each letter having the same probability that it has in the natural language.<sup>5</sup> Thus, in the first-order approximation to English, E is chosen with probability .12 (its frequency in normal English) and W with probability .02, but there is no influence between adjacent letters and no tendency to form the preferred

<sup>5</sup>Letter, digram and trigram frequencies are given in *Secret and Urgent* by Fletcher Pratt, Blue Ribbon Books, 1939. Word frequencies are tabulated in *Relative Frequency of English Speech Sounds*, G. Dewey, Harvard University Press, 1923.

{6}------------------------------------------------

digrams such as TH, ED, etc. In the second-order approximation, digram structure is introduced. After a letter is chosen, the next one is chosen in accordance with the frequencies with which the various letters follow the first one. This requires a table of digram frequencies  $p_i(j)$ . In the third-order approximation, trigram structure is introduced. Each letter is chosen with probabilities which depend on the preceding two letters.

### 3. THE SERIES OF APPROXIMATIONS TO ENGLISH

To give a visual idea of how this series of processes approaches a language, typical sequences in the approximations to English have been constructed and are given below. In all cases we have assumed a 27-symbol “alphabet,” the 26 letters and a space.

1. Zero-order approximation (symbols independent and equiprobable).

XFOML RXKHRJFFJUJ ZLPWCFWKCYJ FFJEYVKCQSGHYD QPAAMKBZAACIBZL-HJQD.

2. First-order approximation (symbols independent but with frequencies of English text).

OCRO HLI RGWR NMIELWIS EU LL NBNESEBYA TH EEI ALHENHTTPA OOBTTVA NAH BRL.

3. Second-order approximation (digram structure as in English).

ON IE ANTSOUTINYS ARE T INCTORE ST BE S DEAMY ACHIN D ILONASIVE TU-COOWE AT TEASONARE FUSO TIZIN ANDY TOBE SEACE CTISBE.

4. Third-order approximation (trigram structure as in English).

IN NO IST LAT WHEY CRATICCT FROURE BIRS GROCID PONDENOME OF DEMONS-TURES OF THE REPTAGIN IS REGOACHTIONA OF CRE.

5. First-order word approximation. Rather than continue with tetragram, . . . ,  $n$ -gram structure it is easier and better to jump at this point to word units. Here words are chosen independently but with their appropriate frequencies.

REPRESENTING AND SPEEDILY IS AN GOOD APT OR COME CAN DIFFERENT NATURAL HERE HE THE A IN CAME THE TO OF TO EXPERT GRAY COME TO FURNISHES THE LINE MESSAGE HAD BE THESE.

6. Second-order word approximation. The word transition probabilities are correct but no further structure is included.

THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS POINT IS THEREFORE ANOTHER METHOD FOR THE LETTERS THAT THE TIME OF WHO EVER TOLD THE PROBLEM FOR AN UNEXPECTED.

The resemblance to ordinary English text increases quite noticeably at each of the above steps. Note that these samples have reasonably good structure out to about twice the range that is taken into account in their construction. Thus in (3) the statistical process insures reasonable text for two-letter sequences, but four-letter sequences from the sample can usually be fitted into good sentences. In (6) sequences of four or more words can easily be placed in sentences without unusual or strained constructions. The particular sequence of ten words “attack on an English writer that the character of this” is not at all unreasonable. It appears then that a sufficiently complex stochastic process will give a satisfactory representation of a discrete source.

The first two samples were constructed by the use of a book of random numbers in conjunction with (for example 2) a table of letter frequencies. This method might have been continued for (3), (4) and (5), since digram, trigram and word frequency tables are available, but a simpler equivalent method was used.

{7}------------------------------------------------

To construct (3) for example, one opens a book at random and selects a letter at random on the page. This letter is recorded. The book is then opened to another page and one reads until this letter is encountered. The succeeding letter is then recorded. Turning to another page this second letter is searched for and the succeeding letter recorded, etc. A similar process was used for (4), (5) and (6). It would be interesting if further approximations could be constructed, but the labor involved becomes enormous at the next stage.

### 4. GRAPHICAL REPRESENTATION OF A MARKOFF PROCESS

Stochastic processes of the type described above are known mathematically as discrete Markoff processes and have been extensively studied in the literature.<sup>6</sup> The general case can be described as follows: There exist a finite number of possible "states" of a system;  $S_1, S_2, \dots, S_n$ . In addition there is a set of transition probabilities;  $p_i(j)$  the probability that if the system is in state  $S_i$  it will next go to state  $S_j$ . To make this Markoff process into an information source we need only assume that a letter is produced for each transition from one state to another. The states will correspond to the "residue of influence" from preceding letters.

The situation can be represented graphically as shown in Figs. 3, 4 and 5. The "states" are the junction

![Figure 3: A directed graph with five states labeled A, B, C, D, and E. State A is the central node. Transitions are: A to A (labeled 4), A to B (labeled 1), B to C (labeled 2), C to D (labeled 2), D to E (labeled 1), and E to A (labeled 1).](35a7554182eb055209552843f341a1ae_img.jpg)

Figure 3: A directed graph with five states labeled A, B, C, D, and E. State A is the central node. Transitions are: A to A (labeled 4), A to B (labeled 1), B to C (labeled 2), C to D (labeled 2), D to E (labeled 1), and E to A (labeled 1).

Fig. 3—A graph corresponding to the source in example B.

points in the graph and the probabilities and letters produced for a transition are given beside the corresponding line. Figure 3 is for the example B in Section 2, while Fig. 4 corresponds to the example C. In Fig. 3

![Figure 4: A directed graph with five states labeled A, B, C, D, and E. State A is the top node. Transitions are: A to C (labeled 2), C to D (labeled 1), D to B (labeled 4), B to E (labeled 5), E to A (labeled 5), A to B (labeled 8), and a self-loop on state B (labeled 5).](07b17a620c75522d53916a11e12d1bff_img.jpg)

Figure 4: A directed graph with five states labeled A, B, C, D, and E. State A is the top node. Transitions are: A to C (labeled 2), C to D (labeled 1), D to B (labeled 4), B to E (labeled 5), E to A (labeled 5), A to B (labeled 8), and a self-loop on state B (labeled 5).

Fig. 4—A graph corresponding to the source in example C.

there is only one state since successive letters are independent. In Fig. 4 there are as many states as letters. If a trigram example were constructed there would be at most  $n^2$  states corresponding to the possible pairs of letters preceding the one being chosen. Figure 5 is a graph for the case of word structure in example D. Here S corresponds to the "space" symbol.

### 5. ERGODIC AND MIXED SOURCES

As we have indicated above a discrete source for our purposes can be considered to be represented by a Markoff process. Among the possible discrete Markoff processes there is a group with special properties of significance in communication theory. This special class consists of the "ergodic" processes and we shall call the corresponding sources ergodic sources. Although a rigorous definition of an ergodic process is somewhat involved, the general idea is simple. In an ergodic process every sequence produced by the process

<sup>6</sup>For a detailed treatment see M. Fréchet, *Méthode des fonctions arbitraires. Théorie des événements en chaîne dans le cas d'un nombre fini d'états possibles*. Paris, Gauthier-Villars, 1938.

{8}------------------------------------------------

is the same in statistical properties. Thus the letter frequencies, digram frequencies, etc., obtained from particular sequences, will, as the lengths of the sequences increase, approach definite limits independent of the particular sequence. Actually this is not true of every sequence but the set for which it is false has probability zero. Roughly the ergodic property means statistical homogeneity.

All the examples of artificial languages given above are ergodic. This property is related to the structure of the corresponding graph. If the graph has the following two properties<sup>7</sup> the corresponding process will be ergodic:

1. The graph does not consist of two isolated parts A and B such that it is impossible to go from junction points in part A to junction points in part B along lines of the graph in the direction of arrows and also impossible to go from junctions in part B to junctions in part A.
2. A closed series of lines in the graph with all arrows on the lines pointing in the same orientation will be called a "circuit." The "length" of a circuit is the number of lines in it. Thus in Fig. 5 series BEBES is a circuit of length 5. The second property required is that the greatest common divisor of the lengths of all circuits in the graph be one.

![A directed graph with 10 nodes. The nodes are arranged in a roughly circular fashion with some internal connections. The edges are labeled with letters A, B, C, D, E, and S. The graph is highly connected, with many edges pointing towards a central node on the right. There are several cycles, including a prominent one labeled BEBES.](b3baf3a29b67c7425d2562ddbc52f0cc_img.jpg)

A directed graph with 10 nodes. The nodes are arranged in a roughly circular fashion with some internal connections. The edges are labeled with letters A, B, C, D, E, and S. The graph is highly connected, with many edges pointing towards a central node on the right. There are several cycles, including a prominent one labeled BEBES.

Fig. 5—A graph corresponding to the source in example D.

If the first condition is satisfied but the second one violated by having the greatest common divisor equal to  $d > 1$ , the sequences have a certain type of periodic structure. The various sequences fall into  $d$  different classes which are statistically the same apart from a shift of the origin (i.e., which letter in the sequence is called letter 1). By a shift of from 0 up to  $d - 1$  any sequence can be made statistically equivalent to any other. A simple example with  $d = 2$  is the following: There are three possible letters  $a, b, c$ . Letter  $a$  is followed with either  $b$  or  $c$  with probabilities  $\frac{1}{3}$  and  $\frac{2}{3}$  respectively. Either  $b$  or  $c$  is always followed by letter  $a$ . Thus a typical sequence is

*a b a c a c a c a b a c a b a b a c a c*.

This type of situation is not of much importance for our work.

If the first condition is violated the graph may be separated into a set of subgraphs each of which satisfies the first condition. We will assume that the second condition is also satisfied for each subgraph. We have in this case what may be called a "mixed" source made up of a number of pure components. The components correspond to the various subgraphs. If  $L_1, L_2, L_3, \dots$  are the component sources we may write

$$L = p_1 L_1 + p_2 L_2 + p_3 L_3 + \dots$$

<sup>7</sup>These are restatements in terms of the graph of conditions given in Fréchet.

{9}------------------------------------------------

where  $p_i$  is the probability of the component source  $L_i$ .

Physically the situation represented is this: There are several different sources  $L_1, L_2, L_3, \dots$  which are each of homogeneous statistical structure (i.e., they are ergodic). We do not know *a priori* which is to be used, but once the sequence starts in a given pure component  $L_i$ , it continues indefinitely according to the statistical structure of that component.

As an example one may take two of the processes defined above and assume  $p_1 = .2$  and  $p_2 = .8$ . A sequence from the mixed source

$$L = .2L_1 + .8L_2$$

would be obtained by choosing first  $L_1$  or  $L_2$  with probabilities  $.2$  and  $.8$  and after this choice generating a sequence from whichever was chosen.

Except when the contrary is stated we shall assume a source to be ergodic. This assumption enables one to identify averages along a sequence with averages over the ensemble of possible sequences (the probability of a discrepancy being zero). For example the relative frequency of the letter A in a particular infinite sequence will be, with probability one, equal to its relative frequency in the ensemble of sequences.

If  $P_i$  is the probability of state  $i$  and  $p_i(j)$  the transition probability to state  $j$ , then for the process to be stationary it is clear that the  $P_i$  must satisfy equilibrium conditions:

$$P_j = \sum_i P_i p_i(j).$$

In the ergodic case it can be shown that with any starting conditions the probabilities  $P_j(N)$  of being in state  $j$  after  $N$  symbols, approach the equilibrium values as  $N \rightarrow \infty$ .

### 6. CHOICE, UNCERTAINTY AND ENTROPY

We have represented a discrete information source as a Markoff process. Can we define a quantity which will measure, in some sense, how much information is “produced” by such a process, or better, at what rate information is produced?

Suppose we have a set of possible events whose probabilities of occurrence are  $p_1, p_2, \dots, p_n$ . These probabilities are known but that is all we know concerning which event will occur. Can we find a measure of how much “choice” is involved in the selection of the event or of how uncertain we are of the outcome?

If there is such a measure, say  $H(p_1, p_2, \dots, p_n)$ , it is reasonable to require of it the following properties:

1.  $H$  should be continuous in the  $p_i$ .
2. If all the  $p_i$  are equal,  $p_i = \frac{1}{n}$ , then  $H$  should be a monotonic increasing function of  $n$ . With equally likely events there is more choice, or uncertainty, when there are more possible events.
3. If a choice be broken down into two successive choices, the original  $H$  should be the weighted sum of the individual values of  $H$ . The meaning of this is illustrated in Fig. 6. At the left we have three

![Figure 6: Decomposition of a choice from three possibilities. The diagram shows two decision trees. The left tree starts at a single point and branches out to three terminal points with probabilities 1/2, 1/3, and 1/6. The right tree starts at a single point, branches into two intermediate points with probabilities 1/2 and 1/2. From the top intermediate point, it branches to two terminal points with probabilities 1/2 and 1/3. From the bottom intermediate point, it branches to two terminal points with probabilities 2/3 and 1/6. The final terminal probabilities on the right are 1/4, 1/6, 1/3, and 1/6.](ee8536b235eb6aad21e2048fd5308900_img.jpg)

Figure 6: Decomposition of a choice from three possibilities. The diagram shows two decision trees. The left tree starts at a single point and branches out to three terminal points with probabilities 1/2, 1/3, and 1/6. The right tree starts at a single point, branches into two intermediate points with probabilities 1/2 and 1/2. From the top intermediate point, it branches to two terminal points with probabilities 1/2 and 1/3. From the bottom intermediate point, it branches to two terminal points with probabilities 2/3 and 1/6. The final terminal probabilities on the right are 1/4, 1/6, 1/3, and 1/6.

Fig. 6—Decomposition of a choice from three possibilities.

possibilities  $p_1 = \frac{1}{2}$ ,  $p_2 = \frac{1}{3}$ ,  $p_3 = \frac{1}{6}$ . On the right we first choose between two possibilities each with probability  $\frac{1}{2}$ , and if the second occurs make another choice with probabilities  $\frac{2}{3}$ ,  $\frac{1}{3}$ . The final results have the same probabilities as before. We require, in this special case, that

$$H\left(\frac{1}{2}, \frac{1}{3}, \frac{1}{6}\right) = H\left(\frac{1}{2}, \frac{1}{2}\right) + \frac{1}{2}H\left(\frac{2}{3}, \frac{1}{3}\right).$$

The coefficient  $\frac{1}{2}$  is because this second choice only occurs half the time.

 Rest of paper (reference and Appendix) is removed.
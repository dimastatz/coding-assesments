Given a binary file that represents a memory dump from some OS. Memory is allocated in blocks of any length. 
Blocks can contain pointers to other blocks. The so-called root block begins at offset 0 in the file. 
It references other blocks, which reference other blocks, and so on. Any memory that belongs to a block reachable from the root block by any number of hops, is considered used. Conversely, the remaining memory is unused. Someone wrote a hidden message in that unused memory. Your task is to extract the hidden message. 
A block contains the following, in order:

1.Length of the block as varint, including the size of this very field.
2.Zero or more pointers as varints.
3.A zero byte (may be omitted if there is no payload).
4.Zero or more arbitrary bytes (payload).

Varint is a variable-length encoding for unsigned integers. It encodeslarger numbers with longer byte sequences. 
See https://developers.google.com/protocol-buffers/docs/encoding#varints (only the Base 128 Varints section) for details.

A pointer is an offset within the memory dump. It always points to the beginning of a block, never into the middle of one. 
Because a zero terminates the sequence of pointers, a block cannot contain a pointer to the root block, 
which has offset 0. A block can contain any number of pointers to any blocks other than the root block. 
A block can reference the same block more than once. Block references may form loops. A block can reference itself. 
The smallest valid block is just the byte 01 (it only contains the length field).

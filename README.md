# Time-stamp-ordering-protocol-in-DBMS
The timestamp-ordering protocol ensures serializability among transactions in their conflicting read and write operations. This is the responsibility of the protocol system that the conflicting pair of tasks should be executed according to the timestamp values of the transactions.

A conflict occurs when an older transaction tries to read/write a value already read or written by a younger transaction. Read or write proceeds only if the last update on that data item was carried out by an older transaction.

Otherwise, the transaction requesting read/write is restarted and gives a new timestamp. Here no locks are used so no deadlock.

- The timestamp of transaction Ti is denoted as TS(Ti).
* Read time-stamp of data-item X is denoted by R-timestamp(X).
+ Write time-stamp of data-item X is denoted by W-timestamp(X).

These timestamps are updated after a successful read/write operation on data item X.

Older transactions get priority over younger transactions in the event of conflict operation. Conflict is resolved by rolling back and restarting transactions.

## Rules for a transaction

To ensure serializability following rules are used −

### Rule 1 − If a transaction Ti issues a read(X) operation.

If TS(Ti) < W-timestamp(X)
Operation rejected.

If TS(Ti) >= W-timestamp(X)
Operation executed.

All data-item timestamps updated.

### Rule 2 − If a transaction Ti issues a write(X) operation.

If TS(Ti) < R-timestamp(X)
Operation rejected.

If TS(Ti) < W-timestamp(X)
Operation rejected and Ti rolled back.

Otherwise, the operation is executed.

## To Run 

1. Open terminal and go to directory where file is stored.

2. Type Command 
```

python3 file_name.py
```
3. Give Input

- 'st1; st2; w1(A); r1(B); r2(B); c1; c2'.

* ‘st1; st2; r1(A); r2(B); w1(A); r2(B); c1; c2;’.

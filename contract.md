# Hợp đồng giao diện giữa các module

Quy ước: hàm kiểm tra trả về `(ok: bool, reason: str)`, lý do bằng tiếng Việt. Hash là chuỗi hex 64 ký tự. Timestamp là số nguyên.

| File | Hàm / lớp | Phụ trách |
|---|---|---|
| crypto/hashing.py | sha256_hex(data)->str; avalanche(a,b)->dict; bruteforce(target,charset,max_len)->dict | Crypto A |
| crypto/wallet.py | Wallet.generate(); wallet.address; wallet.sign(msg_hash)->hex; verify(pubkey,msg_hash,sig)->bool | Crypto B |
| core/transaction.py | Transaction(sender_pub,receiver,amount,nonce,timestamp,signature); hash(); sign(wallet); is_signature_valid() | Trưởng nhóm |
| crypto/merkle.py | merkle_root(hashes)->str; merkle_proof(hashes,index)->list; verify_proof(leaf,proof,root)->bool | Crypto A |
| core/mempool.py | Mempool.add(tx,chain)->(ok,reason); take(n); remove(txs) | Crypto B |
| core/block.py | BlockHeader(version,prev_hash,merkle_root,timestamp,difficulty,nonce); Block(header,transactions); hash() | Blockchain |
| core/pow.py | mine(block,stop_event=None)->(nonce,attempts,seconds); is_pow_valid(block)->bool | Blockchain |
| core/blockchain.py | Blockchain.add_block(block)->(ok,reason); is_chain_valid(); balance_of(addr); total_work() | Trưởng nhóm |
| network/node.py, miner.py | Node.receive_tx/receive_block/broadcast; Miner.start()/stop() | Network |

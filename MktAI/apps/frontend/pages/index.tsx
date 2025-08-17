import { useState } from 'react'

export default function Home() {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    const res = await fetch('http://localhost:8000/run_graph', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ account: input })
    });
    const data = await res.json();
    setMessages([...messages, JSON.stringify(data)]);
  };

  return (
    <div>
      <h1>MktAI Chat</h1>
      <div>{messages.map((m,i) => <pre key={i}>{m}</pre>)}</div>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

"use client";
import { useState, useEffect } from 'react';
import Navbar from '@/components/Navbar';

export default function Explorer() {
    const [data, setData] = useState<any>(null);

    useEffect(() => {
        fetch('http://localhost:8000/api/explorer')
            .then(res => res.json())
            .then(data => setData(data))
            .catch(err => console.error(err));
    }, []);

    if (!data) return <div className="min-h-screen text-white pt-20 text-center">Loading...</div>;

    return (
        <div className="min-h-screen text-white pt-20">
            <Navbar />
            <div className="max-w-screen-xl mx-auto p-4">
                <h1 className="text-3xl font-bold mb-2 text-purple-400">Blockchain Explorer</h1>
                <p className="text-gray-400 mb-8">Latest Block: <span className="text-white font-mono">{data.latest_block}</span></p>

                <div className="space-y-4">
                    {data.certificates.map((cert: any, index: number) => (
                        <div key={index} className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700 hover:border-purple-500 transition">
                            <div className="flex justify-between items-start mb-2">
                                <span className="bg-purple-900 text-purple-200 text-xs font-medium px-2.5 py-0.5 rounded">Transaction</span>
                                <span className="text-xs text-gray-500">{cert.timestamp}</span>
                            </div>
                            <h3 className="text-lg font-bold text-white mb-1">Hash: <span className="font-mono text-sm text-gray-400 break-all">{cert.hash}</span></h3>
                            <div className="grid grid-cols-2 gap-4 mt-4 text-sm text-gray-300">
                                <div><span className="text-gray-500">Student:</span> {cert.student_name}</div>
                                <div><span className="text-gray-500">Institute:</span> {cert.institute}</div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

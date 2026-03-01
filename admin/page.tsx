"use client";
import { useState, useEffect } from 'react';
import Navbar from '@/components/Navbar';

export default function AdminDashboard() {
    const [stats, setStats] = useState<any>(null);

    useEffect(() => {
        fetch('http://localhost:8000/api/admin/stats')
            .then(res => res.json())
            .then(data => setStats(data))
            .catch(err => console.error(err));
    }, []);

    if (!stats) return <div className="min-h-screen text-white pt-20 text-center">Loading...</div>;

    return (
        <div className="min-h-screen text-white pt-20">
            <Navbar />
            <div className="max-w-screen-xl mx-auto p-4">
                <h1 className="text-3xl font-bold mb-8 text-blue-400">Admin Dashboard</h1>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700">
                        <h3 className="text-gray-400">Total Issued</h3>
                        <p className="text-4xl font-bold text-white">{stats.total_issued}</p>
                    </div>
                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700">
                        <h3 className="text-gray-400">Total Verified</h3>
                        <p className="text-4xl font-bold text-green-400">{stats.total_verified}</p>
                    </div>
                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700">
                        <h3 className="text-gray-400">Fake Attempts</h3>
                        <p className="text-4xl font-bold text-red-400">{stats.fake_attempts}</p>
                    </div>
                </div>

                <h2 className="text-xl font-bold mb-4 text-gray-300">Recent Activity</h2>
                <div className="bg-gray-800/60 backdrop-blur-md rounded-lg overflow-hidden border border-gray-700">
                    <table className="w-full text-left text-gray-400">
                        <thead className="bg-gray-700/50 text-gray-200 uppercase text-sm">
                            <tr>
                                <th className="p-4">Student</th>
                                <th className="p-4">Course</th>
                                <th className="p-4">Institute</th>
                                <th className="p-4">Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {stats.recent_activity.map((cert: any, index: number) => (
                                <tr key={index} className="border-b border-gray-700 hover:bg-gray-700/50 transition">
                                    <td className="p-4 font-medium text-white">{cert.student_name}</td>
                                    <td className="p-4">{cert.course}</td>
                                    <td className="p-4">{cert.institute}</td>
                                    <td className="p-4 text-green-400">{cert.status}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}
